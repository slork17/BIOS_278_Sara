#!/usr/bin/env python3
"""
BIDS-Compatible Brain Image Visualization

This script processes anatomical MRI images from a BIDS-structured dataset
and creates visualizations for quality control.

BIDS Format Expected:
    dataset/
        sub-01/
            anat/
                sub-01_T1w.nii.gz
                sub-01_T2w.nii.gz
        sub-02/
            anat/
                sub-02_T1w.nii.gz

Usage:
    # Process single subject
    python plot_brain_bids.py --bids-dir /path/to/dataset --subject 01
    
    # Process all subjects
    python plot_brain_bids.py --bids-dir /path/to/dataset --all
    
    # Specific modality
    python plot_brain_bids.py --bids-dir /path/to/dataset --subject 01 --modality T2w

Author: Your Name
Date: 2024-11-16
Version: 1.0.0
"""

import argparse
import logging
from pathlib import Path
import json
from datetime import datetime
import sys

import nibabel as nib
import nilearn
from nilearn import plotting
import matplotlib
matplotlib.use('Agg')


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BIDSDataset:
    """Handle BIDS dataset structure and validation."""
    
    def __init__(self, bids_dir):
        """
        Initialize BIDS dataset handler.
        
        Parameters
        ----------
        bids_dir : Path
            Root directory of BIDS dataset
        """
        self.bids_dir = Path(bids_dir)
        self.validate_bids_structure()
    
    def validate_bids_structure(self):
        """Validate that directory follows BIDS structure."""
        if not self.bids_dir.exists():
            raise FileNotFoundError(f"BIDS directory not found: {self.bids_dir}")
        
        # Check for dataset_description.json (BIDS requirement)
        desc_file = self.bids_dir / 'dataset_description.json'
        if not desc_file.exists():
            logger.warning(
                f"No dataset_description.json found. "
                f"This may not be a valid BIDS dataset."
            )
        else:
            with open(desc_file) as f:
                self.dataset_info = json.load(f)
                logger.info(f"Dataset: {self.dataset_info.get('Name', 'Unknown')}")
    
    def get_subjects(self):
        """
        Get list of all subjects in dataset.
        
        Returns
        -------
        list of str
            Subject IDs (without 'sub-' prefix)
        """
        subject_dirs = sorted(self.bids_dir.glob('sub-*'))
        subjects = [d.name.replace('sub-', '') for d in subject_dirs if d.is_dir()]
        logger.info(f"Found {len(subjects)} subjects: {subjects}")
        return subjects
    
    def get_anat_files(self, subject, modality='T1w'):
        """
        Get anatomical files for a subject.
        
        Parameters
        ----------
        subject : str
            Subject ID (without 'sub-' prefix)
        modality : str
            MRI modality (T1w, T2w, etc.)
            
        Returns
        -------
        list of Path
            Paths to anatomical NIfTI files
        """
        subject_dir = self.bids_dir / f'sub-{subject}' / 'anat'
        
        if not subject_dir.exists():
            raise FileNotFoundError(f"No anat directory for sub-{subject}")
        
        # Find files matching pattern
        pattern = f'sub-{subject}_*{modality}.nii.gz'
        files = sorted(subject_dir.glob(pattern))
        
        if not files:
            raise FileNotFoundError(
                f"No {modality} files found for sub-{subject} in {subject_dir}"
            )
        
        return files


def process_subject(bids_dir, subject, modality, output_dir):
    """
    Process anatomical images for one subject.
    
    Parameters
    ----------
    bids_dir : Path
        BIDS dataset directory
    subject : str
        Subject ID
    modality : str
        MRI modality
    output_dir : Path
        Output directory
    """
    logger.info(f"Processing sub-{subject}, modality: {modality}")
    
    # Initialize BIDS dataset
    dataset = BIDSDataset(bids_dir)
    
    # Get anatomical files
    anat_files = dataset.get_anat_files(subject, modality)
    
    # Create subject output directory
    subject_output = output_dir / f'sub-{subject}'
    subject_output.mkdir(parents=True, exist_ok=True)
    
    # Process each anatomical file
    for anat_file in anat_files:
        logger.info(f"Processing: {anat_file.name}")
        
        # Load image
        img = nib.load(str(anat_file))
        
        # Create filename base (BIDS-style)
        base_name = anat_file.stem.replace('.nii', '')
        
        # Generate orthogonal view
        display = plotting.plot_anat(
            img,
            title=f"sub-{subject} {modality}",
            display_mode='ortho',
            annotate=True,
            draw_cross=True
        )
        output_file = subject_output / f'{base_name}_ortho.png'
        display.savefig(str(output_file), dpi=300)
        display.close()
        logger.info(f"Saved: {output_file}")
        
        # Generate slice view
        display = plotting.plot_anat(
            img,
            title=f"sub-{subject} {modality}",
            display_mode='z',
            cut_coords=7,
            annotate=True
        )
        output_file = subject_output / f'{base_name}_slices.png'
        display.savefig(str(output_file), dpi=300)
        display.close()
        logger.info(f"Saved: {output_file}")
    
    # Save processing metadata
    metadata = {
        'timestamp': datetime.now().isoformat(),
        'subject': subject,
        'modality': modality,
        'files_processed': [str(f) for f in anat_files],
        'software_versions': {
            'python': sys.version,
            'nibabel': nib.__version__,
            'nilearn': nilearn.__version__,
        }
    }
    
    metadata_file = subject_output / f'sub-{subject}_{modality}_metadata.json'
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    logger.info(f"Completed sub-{subject}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Process BIDS anatomical MRI data',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--bids-dir',
        type=Path,
        required=True,
        help='Path to BIDS dataset directory'
    )
    
    parser.add_argument(
        '--subject',
        type=str,
        help='Subject ID to process (without sub- prefix)'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all subjects in dataset'
    )
    
    parser.add_argument(
        '--modality',
        type=str,
        default='T1w',
        choices=['T1w', 'T2w', 'FLAIR', 'PD'],
        help='MRI modality to process (default: T1w)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('derivatives/visualizations'),
        help='Output directory (default: derivatives/visualizations)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.subject and not args.all:
        parser.error("Must specify either --subject or --all")
    
    # Initialize dataset
    dataset = BIDSDataset(args.bids_dir)
    
    # Determine subjects to process
    if args.all:
        subjects = dataset.get_subjects()
    else:
        subjects = [args.subject]
    
    # Create output directory
    output_dir = args.bids_dir / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Processing {len(subjects)} subject(s)")
    
    # Process each subject
    for subject in subjects:
        try:
            process_subject(args.bids_dir, subject, args.modality, output_dir)
        except Exception as e:
            logger.error(f"Error processing sub-{subject}: {e}", exc_info=True)
            continue
    
    logger.info("All processing complete!")


if __name__ == '__main__':
    main()
