#!/usr/bin/env python3
"""
Brain Image Visualization Script

This script loads a structural brain MRI image in NIfTI format and creates
anatomical visualizations using nilearn.

Usage:
    python plot_brain_image.py --input <path_to_nifti> --output <output_dir>

Example:
    python plot_brain_image.py --input data/sub-01/anat/sub-01_T1w.nii.gz --output results/

Requirements:
    - Python 3.8+
    - nilearn >= 0.10.0
    - nibabel >= 4.0.0
    - matplotlib >= 3.5.0

Author: Your Name
Date: 2024-11-16
Version: 1.0.0
"""

import argparse
import logging
import sys
from pathlib import Path
from datetime import datetime
import json

import nibabel as nib
import nilearn
from nilearn import plotting
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server environments
import matplotlib.pyplot as plt


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def validate_input_image(image_path):
    """
    Validate that the input image exists and is a valid NIfTI file.
    
    Parameters
    ----------
    image_path : Path
        Path to the NIfTI image file
        
    Returns
    -------
    nibabel.Nifti1Image
        Loaded NIfTI image
        
    Raises
    ------
    FileNotFoundError
        If image file does not exist
    ValueError
        If image cannot be loaded or has invalid dimensions
    """
    if not image_path.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    if not str(image_path).endswith(('.nii', '.nii.gz')):
        raise ValueError(f"File must be NIfTI format (.nii or .nii.gz): {image_path}")
    
    try:
        img = nib.load(str(image_path))
        logger.info(f"Loaded image with shape: {img.shape}")
        logger.info(f"Image affine:\n{img.affine}")
    except Exception as e:
        raise ValueError(f"Failed to load NIfTI image: {e}")
    
    # Validate dimensions (expect 3D or 4D image)
    if len(img.shape) < 3 or len(img.shape) > 4:
        raise ValueError(f"Expected 3D or 4D image, got shape: {img.shape}")
    
    return img


def create_output_directory(output_dir):
    """
    Create output directory if it doesn't exist.
    
    Parameters
    ----------
    output_dir : Path
        Path to output directory
        
    Returns
    -------
    Path
        Validated output directory path
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {output_dir}")
    return output_dir


def plot_anatomical_image(img, output_path, title=None):
    """
    Create and save anatomical visualization of brain image.
    
    Parameters
    ----------
    img : nibabel.Nifti1Image
        Brain image to visualize
    output_path : Path
        Path where plot will be saved
    title : str, optional
        Title for the plot
    """
    logger.info(f"Creating anatomical plot: {output_path}")
    
    display = plotting.plot_anat(
        img,
        title=title,
        display_mode='ortho',
        cut_coords=None,
        annotate=True,
        draw_cross=True
    )
    
    display.savefig(str(output_path), dpi=300)
    display.close()
    logger.info(f"Saved anatomical plot to: {output_path}")


def plot_slices(img, output_path, title=None):
    """
    Create and save multi-slice visualization.
    
    Parameters
    ----------
    img : nibabel.Nifti1Image
        Brain image to visualize
    output_path : Path
        Path where plot will be saved
    title : str, optional
        Title for the plot
    """
    logger.info(f"Creating slice plot: {output_path}")
    
    display = plotting.plot_anat(
        img,
        title=title,
        display_mode='z',
        cut_coords=7,
        annotate=True
    )
    
    display.savefig(str(output_path), dpi=300)
    display.close()
    logger.info(f"Saved slice plot to: {output_path}")


def save_metadata(output_dir, image_path, img):
    """
    Save processing metadata for reproducibility.
    
    Parameters
    ----------
    output_dir : Path
        Output directory
    image_path : Path
        Input image path
    img : nibabel.Nifti1Image
        Loaded image
    """
    metadata = {
        'timestamp': datetime.now().isoformat(),
        'script_version': '1.0.0',
        'input_file': str(image_path.absolute()),
        'image_shape': list(img.shape),
        'image_dtype': str(img.get_data_dtype()),
        'voxel_size': img.header.get_zooms()[:3],
        'software_versions': {
            'python': sys.version,
            'nibabel': nib.__version__,
            'nilearn': nilearn.__version__,
            'matplotlib': matplotlib.__version__
        }
    }
    
    metadata_path = output_dir / 'processing_metadata.json'
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2, default=str)
    
    logger.info(f"Saved metadata to: {metadata_path}")


def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns
    -------
    argparse.Namespace
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Visualize brain MRI images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Single subject
    python plot_brain_image.py -i data/sub-01/anat/sub-01_T1w.nii.gz -o results/sub-01/

    # With custom title
    python plot_brain_image.py -i brain.nii.gz -o outputs/ -t "Subject 001 T1w"
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        type=Path,
        required=True,
        help='Path to input NIfTI image (.nii or .nii.gz)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        required=True,
        help='Path to output directory'
    )
    
    parser.add_argument(
        '-t', '--title',
        type=str,
        default=None,
        help='Title for the plots (default: filename)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    return parser.parse_args()


def main():
    """
    Main execution function.
    """
    # Parse arguments
    args = parse_arguments()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Log start
    logger.info("="*60)
    logger.info("Brain Image Visualization Script v1.0.0")
    logger.info("="*60)
    logger.info(f"Input image: {args.input}")
    logger.info(f"Output directory: {args.output}")
    
    try:
        # Validate input
        img = validate_input_image(args.input)
        
        # Create output directory
        output_dir = create_output_directory(args.output)
        
        # Generate title if not provided
        title = args.title if args.title else args.input.stem
        
        # Create base filename from input
        base_name = args.input.stem.replace('.nii', '')
        
        # Generate plots
        plot_anatomical_image(
            img,
            output_dir / f'{base_name}_ortho.png',
            title=f'{title} - Orthogonal View'
        )
        
        plot_slices(
            img,
            output_dir / f'{base_name}_slices.png',
            title=f'{title} - Axial Slices'
        )
        
        # Save metadata
        save_metadata(output_dir, args.input, img)
        
        logger.info("="*60)
        logger.info("Processing completed successfully!")
        logger.info(f"Results saved to: {output_dir}")
        logger.info("="*60)
        
    except Exception as e:
        logger.error(f"Error during processing: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()