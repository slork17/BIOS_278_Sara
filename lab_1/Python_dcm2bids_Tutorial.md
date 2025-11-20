# Python Environment Setup and DICOM to BIDS Conversion Tutorial

**Course:** BIOS 278 - Reproducibility and Data Science in Computational Brain Image Analysis  
**Stanford University**

---

## 📋 Overview

This tutorial will guide you through:
1. Creating a dedicated Python virtual environment
2. Installing dcm2niix (DICOM to NIfTI converter)
3. Installing dcm2bids (automated BIDS conversion tool)
4. Following the official dcm2bids tutorial to convert DICOM files to BIDS format

**Estimated Time:** 2-3 hours

---

## 🎯 Learning Objectives

By the end of this tutorial, you will be able to:
- ✅ Create and manage Python virtual environments
- ✅ Install neuroimaging tools using pip
- ✅ Use dcm2niix to convert DICOM files to NIfTI format
- ✅ Create configuration files for dcm2bids
- ✅ Automatically convert and organize neuroimaging data to BIDS standard
- ✅ Troubleshoot common conversion issues

---

## 📦 Prerequisites

### System Requirements
- Python 3.8 or higher
- Command line access (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows)
- Basic familiarity with command line operations
- Text editor (VS Code, Sublime Text, nano, vim, etc.)

### Verify Python Installation

```bash
# Check Python version
python --version
# or
python3 --version
```

**Expected output:** Python 3.8.x or higher

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

---

## Part 1: Setting Up Your Python Environment

### Why Use Virtual Environments?

Virtual environments allow you to:
- **Isolate dependencies** for different projects
- **Avoid version conflicts** between packages
- **Reproduce your setup** on different machines
- **Keep your system Python clean** and organized

### Step 1.1: Create a Virtual Environment

Navigate to your desired working directory:

```bash
# Navigate to your projects folder
cd ~/Documents

# Create a directory for this project
mkdir dcm2bids_tutorial
cd dcm2bids_tutorial
```

Create a virtual environment named `dcm2bids_env`:

```bash
# Using venv (built-in to Python 3)
python3 -m venv dcm2bids_env
```

**What this does:** Creates a folder `dcm2bids_env` containing an isolated Python installation.

### Step 1.2: Activate the Virtual Environment

The activation command differs by operating system:

**macOS/Linux:**
```bash
source dcm2bids_env/bin/activate
```

**Windows (Command Prompt):**
```bash
dcm2bids_env\Scripts\activate
```

**Windows (PowerShell):**
```bash
dcm2bids_env\Scripts\Activate.ps1
```

**Expected result:** Your command prompt should now be prefixed with `(dcm2bids_env)`.

```bash
(dcm2bids_env) user@computer:~/Documents/dcm2bids_tutorial$
```

### Step 1.3: Upgrade pip

Always start with the latest pip version:

```bash
pip install --upgrade pip
```

---

## Part 2: Installing dcm2niix

### What is dcm2niix?

dcm2niix is a tool that converts DICOM files (the standard format for medical imaging) to NIfTI format (commonly used in neuroimaging research). It also creates JSON sidecar files containing important metadata from the DICOM headers.

### Step 2.1: Install dcm2niix

```bash
pip install dcm2niix
```

### Step 2.2: Verify Installation

```bash
dcm2niix --version
```

**Expected output:** Version information like `v1.0.20240202` or similar.

If you encounter issues, you can also install dcm2niix using conda or from pre-compiled binaries:

**Alternative installation methods:**

```bash
# Using conda (if you have Anaconda/Miniconda)
conda install -c conda-forge dcm2niix

# Or download pre-compiled binaries from:
# https://github.com/rordenlab/dcm2niix/releases
```

---

## Part 3: Installing dcm2bids

### What is dcm2bids?

dcm2bids is a tool that automates the process of converting DICOM files to NIfTI files using dcm2niix and then reorganizing the NIfTI files into the Brain Imaging Data Structure (BIDS) format.

### Step 3.1: Install dcm2bids

```bash
pip install dcm2bids
```

### Step 3.2: Verify Installation

Test that all dcm2bids commands are accessible:

```bash
# Main conversion command
dcm2bids --help

# Helper command for creating config files
dcm2bids_helper --help

# Scaffolding command for creating BIDS directory structure
dcm2bids_scaffold --help
```

**Expected output:** Help text for each command showing available options.

### Step 3.3: Check Installed Versions

```bash
pip list | grep dcm2
```

**Expected output:**
```
dcm2bids       3.2.0
dcm2niix       1.0.20240202
```

---

## Part 4: Following the dcm2bids Official Tutorial

Now that you have all the tools installed, let's follow the official dcm2bids tutorial to convert sample DICOM data to BIDS format.

### Step 4.1: Verify Your Environment

Make sure your virtual environment is activated and dcm2bids is accessible:

```bash
# Should show (dcm2bids_env) prefix
echo $PATH | grep dcm2bids_env

# Test dcm2bids command
dcm2bids --help
```

If you get `dcm2bids: command not found`, ensure your virtual environment is activated.

### Step 4.2: Create Tutorial Directory

Create a new directory for the tutorial instead of using real project data:

```bash
# Make sure you're in your project directory
cd ~/Documents/dcm2bids_tutorial

# Create a directory for the tutorial
mkdir dcm2bids-tutorial
cd dcm2bids-tutorial
```

### Step 4.3: Scaffold Your BIDS Project

The dcm2bids_scaffold command creates a basic BIDS directory structure and core files according to the BIDS specification:

```bash
# Create scaffold in a directory called 'bids_project'
dcm2bids_scaffold -o bids_project
```

**Expected output:**
```
bids_project/
├── code/
├── derivatives/
├── sourcedata/
├── CHANGES
├── dataset_description.json
├── participants.json
├── participants.tsv
└── README
```

**What each directory/file is for:**
- `code/`: Analysis scripts and code
- `derivatives/`: Processed/analyzed data
- `sourcedata/`: Original DICOM files
- `dataset_description.json`: Required metadata about your dataset
- `participants.tsv`: Information about each participant
- `README`: Description of your dataset

### Step 4.4: Navigate to Your Project

```bash
cd bids_project
```

### Step 4.5: Download Sample DICOM Data

Download the dcm_qa_nih dataset, which is stable test data used by dcm2niix developers:

**Option 1: Using wget (macOS/Linux):**
```bash
# Download the zip file
wget -O dcm_qa_nih-master.zip https://github.com/neurolabusc/dcm_qa_nih/archive/refs/heads/master.zip

# Extract to sourcedata directory
unzip dcm_qa_nih-master.zip -d sourcedata/

# Rename the directory
mv sourcedata/dcm_qa_nih-master sourcedata/dcm_qa_nih
```

**Option 2: Using Git:**
```bash
# Clone directly into sourcedata
git clone https://github.com/neurolabusc/dcm_qa_nih/ sourcedata/dcm_qa_nih
```

**Option 3: Manual Download:**
1. Go to https://github.com/neurolabusc/dcm_qa_nih
2. Click the green "Code" button and select "Download ZIP"
3. Extract the ZIP file
4. Move the extracted folder to `sourcedata/` and rename it to `dcm_qa_nih`

### Step 4.6: Verify Data Download

```bash
ls sourcedata/dcm_qa_nih/
```

**Expected output:** You should see directories containing DICOM files.

---

## Part 5: Creating the Configuration File

### Step 5.1: Use dcm2bids_helper to Inspect Your Data

The dcm2bids_helper command converts DICOMs to NIfTI and creates JSON sidecar files that you can inspect to build your configuration file:

```bash
# Run helper on the sample data
dcm2bids_helper -d sourcedata/dcm_qa_nih/In/
```

**Expected output:**
```
--- dcm2bids_helper ---
INFO    | dcm2niix version: v1.0.20240202
INFO    | Command: dcm2niix -b y -ba y -z y -f '%3s_%f_%p_%t' -o /path/to/tmp_dcm2bids/helper sourcedata/dcm_qa_nih/In/
INFO    | dcm2niix was successful
```

### Step 5.2: Examine the Helper Output

Look at the JSON sidecar files created in the helper directory:

```bash
ls tmp_dcm2bids/helper/
```

**Expected output:** Multiple `.nii.gz` and `.json` files.

### Step 5.3: Inspect JSON Sidecar Files

Examine the sidecar files to identify unique characteristics of your acquisitions:

```bash
# View a sidecar file (replace with actual filename)
cat tmp_dcm2bids/helper/004_In_DCM2NIIX_regression_test_20180918114023.json
```

Look for fields like:
- `SeriesDescription`: Description of the acquisition
- `SeriesNumber`: Order in the scanning protocol
- `PhaseEncodingDirection`: For fieldmaps
- `EchoTime`, `RepetitionTime`: Timing parameters

**Example JSON content:**
```json
{
    "Modality": "MR",
    "MagneticFieldStrength": 3,
    "Manufacturer": "GE",
    "ManufacturersModelName": "DISCOVERY MR750",
    "SeriesDescription": "Axial EPI-FMRI (Interleaved I to S)",
    "SeriesNumber": 4,
    "AcquisitionTime": "11:40:23.000000",
    "PhaseEncodingDirection": "j-",
    "EchoTime": 0.03,
    "RepetitionTime": 2,
    "FlipAngle": 90
}
```

### Step 5.4: Create Your Configuration File

Create a configuration file in the code directory:

```bash
# Navigate to code directory
cd code

# Create the config file (use your preferred text editor)
nano dcm2bids_config.json
```

**Start with this basic template:**

```json
{
    "descriptions": [
        
    ]
}
```

### Step 5.5: Add Descriptions for Your Acquisitions

For each acquisition you want to convert, add a description with matching criteria:

**Example: Adding a functional MRI acquisition**

First, find a unique identifier in the JSON:
```bash
# Search for "Axial EPI-FMRI" in all JSON files
grep "Axial EPI-FMRI" tmp_dcm2bids/helper/*.json
```

Add the acquisition to your config file:

```json
{
    "descriptions": [
        {
            "datatype": "func",
            "suffix": "bold",
            "criteria": {
                "SeriesDescription": "Axial EPI-FMRI (Interleaved I to S)"
            },
            "sidecar_changes": {
                "TaskName": "rest"
            }
        }
    ]
}
```

**Understanding the configuration fields:**

- **`datatype`**: BIDS data type (`anat`, `func`, `dwi`, `fmap`, etc.)
- **`suffix`**: BIDS suffix (`T1w`, `T2w`, `bold`, `dwi`, etc.)
- **`criteria`**: Dictionary of JSON fields to match
- **`sidecar_changes`**: Metadata to add/modify in the output JSON

### Step 5.6: Add Fieldmap Acquisitions

For fieldmaps, you can use the auto-extract feature to automatically extract entities like direction:

```json
{
    "descriptions": [
        {
            "datatype": "func",
            "suffix": "bold",
            "criteria": {
                "SeriesDescription": "Axial EPI-FMRI (Interleaved I to S)"
            },
            "sidecar_changes": {
                "TaskName": "rest"
            }
        },
        {
            "id": "id_task_rest",
            "datatype": "fmap",
            "suffix": "epi",
            "criteria": {
                "SeriesDescription": "EPI*"
            },
            "sidecar_changes": {
                "IntendedFor": "id_task_rest"
            }
        }
    ]
}
```

**Key concepts for fieldmaps:**

- **`id`**: Unique identifier for linking fieldmaps to functional data
- **`IntendedFor`**: References the `id` of acquisitions this fieldmap corrects
- Wildcards (`*`) can be used in criteria for pattern matching

### Step 5.7: Validate Your JSON

Use an online JSON validator to check for syntax errors:

Go to https://jsonlint.com/ and paste your configuration file to check for:
- Missing or extra commas
- Unmatched brackets `[]` or braces `{}`
- Incorrect quotation marks

**Final configuration file example:**

```json
{
    "descriptions": [
        {
            "datatype": "func",
            "suffix": "bold",
            "criteria": {
                "SeriesDescription": "Axial EPI-FMRI (Interleaved I to S)"
            },
            "sidecar_changes": {
                "TaskName": "rest"
            }
        },
        {
            "id": "id_task_rest",
            "datatype": "fmap",
            "suffix": "epi",
            "criteria": {
                "SeriesDescription": "EPI PE=AP"
            },
            "sidecar_changes": {
                "IntendedFor": "id_task_rest"
            }
        },
        {
            "id": "id_task_rest",
            "datatype": "fmap",
            "suffix": "epi",
            "criteria": {
                "SeriesDescription": "EPI PE=PA"
            },
            "sidecar_changes": {
                "IntendedFor": "id_task_rest"
            }
        }
    ]
}
```

---

## Part 6: Running dcm2bids

### Step 6.1: Navigate Back to Project Root

```bash
cd ~/Documents/dcm2bids_tutorial/dcm2bids-tutorial/bids_project
```

### Step 6.2: Run the Main dcm2bids Command

Run dcm2bids with required options: DICOM directory (-d), participant ID (-p), and config file (-c):

```bash
dcm2bids -d sourcedata/dcm_qa_nih/In/ \
         -p ID01 \
         -c code/dcm2bids_config.json \
         --auto_extract_entities
```

**Command breakdown:**
- `-d`: Directory containing DICOM files
- `-p`: Participant ID (will create `sub-ID01`)
- `-c`: Path to your configuration file
- `--auto_extract_entities`: Automatically extract BIDS entities from JSON

### Step 6.3: Review the Output

dcm2bids prints information about the conversion process and creates log files:

**Expected console output:**
```
--- dcm2bids ---
INFO    | dcm2niix version: v1.0.20240202
INFO    | Participant: sub-ID01
INFO    | Session: None
INFO    | Config: code/dcm2bids_config.json
INFO    | Output: /path/to/bids_project
INFO    | 
INFO    | dcm2niix was successful
INFO    | 
INFO    | Pairing acquisitions
INFO    |   004_In_DCM2NIIX_regression_test_20180918114023.json  →  sub-ID01_task-rest_bold
INFO    |   003_In_EPI_PE=AP_20180918121230.json  →  sub-ID01_dir-AP_epi
INFO    |   004_In_EPI_PE=PA_20180918121230.json  →  sub-ID01_dir-PA_epi
```

### Step 6.4: Examine Your BIDS Dataset

```bash
# View the directory structure
tree sub-ID01/
# Or if tree is not available:
find sub-ID01 -type f
```

**Expected output:**
```
sub-ID01/
├── func/
│   ├── sub-ID01_task-rest_bold.nii.gz
│   └── sub-ID01_task-rest_bold.json
└── fmap/
    ├── sub-ID01_dir-AP_epi.nii.gz
    ├── sub-ID01_dir-AP_epi.json
    ├── sub-ID01_dir-PA_epi.nii.gz
    └── sub-ID01_dir-PA_epi.json
```

### Step 6.5: Check Unpaired Files

Files that weren't matched by your config file remain in the temporary directory:

```bash
ls tmp_dcm2bids/sub-ID01/
```

Review these files to determine if they should be included in your BIDS dataset. If so, update your configuration file and re-run dcm2bids.

### Step 6.6: Review Log Files

Log files are saved in the tmp_dcm2bids/log directory for troubleshooting:

```bash
ls tmp_dcm2bids/log/
cat tmp_dcm2bids/log/sub-ID01_*.log
```

---

## Part 7: Validating Your BIDS Dataset

### Step 7.1: Update dataset_description.json

Edit the dataset description file to include accurate metadata:

```bash
nano dataset_description.json
```

**Update with your information:**
```json
{
    "Name": "dcm2bids Tutorial Dataset",
    "BIDSVersion": "1.9.0",
    "DatasetType": "raw",
    "License": "CC0",
    "Authors": [
        "Your Name"
    ],
    "Acknowledgements": "Data from dcm_qa_nih repository",
    "ReferencesAndLinks": [
        "https://github.com/neurolabusc/dcm_qa_nih"
    ]
}
```

### Step 7.2: Create participants.tsv

Create a participants file describing your subjects:

```bash
nano participants.tsv
```

**Add this content (use actual TABS between columns):**
```tsv
participant_id	age	sex
sub-ID01	30	M
```

### Step 7.3: Validate Using the Online BIDS Validator

1. Go to https://bids-standard.github.io/bids-validator/
2. Click "Select Dataset Folder"
3. Select your `bids_project` directory
4. Review validation results

**Fix any errors reported by the validator.**

### Step 7.4: Optional - Install BIDS Validator Locally

For faster validation, install the validator locally:

```bash
# Using pip
pip install bids-validator

# Validate your dataset
bids-validator bids_project/
```

---

## Part 8: Best Practices and Tips

### Configuration File Best Practices

1. **Start Simple**: Begin with one or two acquisitions, validate, then add more
2. **Use Descriptive IDs**: Name your IDs clearly (e.g., `id_anat_T1`, `id_func_rest`)
3. **Test with One Subject**: Always test your config on a single subject first
4. **Document Your Choices**: Add comments in a separate README explaining your criteria choices
5. **Version Control**: Keep your config files in Git to track changes

### Common Matching Strategies

```json
// Use exact match
"criteria": {
    "SeriesDescription": "Axial T1 MPRAGE"
}

// Use wildcards
"criteria": {
    "SeriesDescription": "*T1*"
}

// Multiple criteria (all must match)
"criteria": {
    "SeriesDescription": "*EPI*",
    "EchoTime": 0.03,
    "SeriesNumber": 4
}

// Numerical comparisons
"criteria": {
    "RepetitionTime": "<=0.0086"
}
```

### Working with Multiple Participants

Create a script to batch process multiple subjects:

```bash
#!/bin/bash
# process_all_subjects.sh

for subject in sub-01 sub-02 sub-03; do
    echo "Processing $subject"
    dcm2bids -d sourcedata/${subject}/dicoms \
             -p ${subject#sub-} \
             -c code/dcm2bids_config.json \
             --auto_extract_entities
done
```

Make it executable and run:
```bash
chmod +x process_all_subjects.sh
./process_all_subjects.sh
```

### Handling Sessions

If you have multiple sessions per subject:

```bash
dcm2bids -d sourcedata/sub-01/ses-01/dicoms \
         -p 01 \
         -s 01 \
         -c code/dcm2bids_config.json
```

This creates: `sub-01/ses-01/anat/`, `sub-01/ses-01/func/`, etc.

---

## Part 9: Troubleshooting

### Issue: dcm2bids command not found

**Solution:**
```bash
# Ensure virtual environment is activated
source dcm2bids_env/bin/activate  # macOS/Linux
# or
dcm2bids_env\Scripts\activate  # Windows

# Verify installation
which dcm2bids
pip list | grep dcm2bids
```

### Issue: No files are being matched

**Solution:**
1. Check your JSON sidecar files in `tmp_dcm2bids/helper/`
2. Verify the exact spelling and capitalization in your criteria
3. Start with a single, very specific criterion
4. Use wildcards (`*`) if appropriate

```bash
# Test your criteria manually
grep "YourSeriesDescription" tmp_dcm2bids/helper/*.json
```

### Issue: Files are matched multiple times

**Solution:**
- Make your criteria more specific
- Add additional matching criteria
- Check SeriesNumber or AcquisitionTime to disambiguate

### Issue: IntendedFor not working

**Solution:**
- Ensure both the fieldmap and target acquisition have matching `id` values
- Verify the `id` exists in your functional/diffusion description
- Check that IntendedFor is in `sidecar_changes`, not at the top level

### Issue: JSON syntax errors

**Solution:**
- Use https://jsonlint.com/ to validate your JSON
- Check for missing commas between elements
- Ensure all brackets and braces are matched
- Use a code editor with JSON validation (VS Code, Sublime Text)

### Issue: Python/pip not found

**Solution:**
```bash
# Try python3 explicitly
python3 -m pip install dcm2bids

# Check your PATH
echo $PATH

# Reinstall Python from python.org if necessary
```

---

## Part 10: Advanced Topics

### Using Custom Entities

Add custom BIDS entities beyond standard ones:

```json
{
    "datatype": "func",
    "suffix": "bold",
    "custom_entities": "acq-highres",
    "criteria": {
        "SeriesDescription": "*EPI_HighRes*"
    }
}
```

Output: `sub-01_acq-highres_task-rest_bold.nii.gz`

### Extracting Entities from Metadata

Automatically extract entities from JSON fields:

```json
{
    "datatype": "func",
    "suffix": "bold",
    "criteria": {
        "SeriesDescription": "*task-*"
    },
    "custom_entities": {
        "task": {
            "regex": "task-([a-zA-Z0-9]+)",
            "from": "SeriesDescription"
        }
    }
}
```

### Modifying dcm2niix Options

Customize dcm2niix behavior in your config:

```json
{
    "dcm2niixOptions": "-b y -ba y -z y -f '%3s_%f_%p_%t'",
    "descriptions": [
        ...
    ]
}
```

Options:
- `-b y`: Create BIDS sidecar JSON
- `-ba y`: Anonymize the data
- `-z y`: Compress output (.nii.gz)
- `-f`: File naming format

### Handling Multi-Echo Data

For multi-echo fMRI:

```json
{
    "datatype": "func",
    "suffix": "bold",
    "criteria": {
        "SeriesDescription": "*ME-EPI*",
        "EchoNumber": 1
    },
    "sidecar_changes": {
        "TaskName": "rest"
    }
}
```

---

## 📝 Summary and Next Steps

### What You've Learned

✅ Created and activated a Python virtual environment  
✅ Installed dcm2niix and dcm2bids using pip  
✅ Used dcm2bids_scaffold to create a BIDS project structure  
✅ Ran dcm2bids_helper to inspect DICOM metadata  
✅ Created a configuration file to match acquisitions  
✅ Converted DICOM data to BIDS-formatted NIfTI  
✅ Validated your BIDS dataset  

### Next Steps

1. **Practice with Your Own Data**
   - Apply what you learned to your research data
   - Create configuration files for your scanning protocols
   - Automate conversion for multiple subjects

2. **Explore BIDS Apps**
   - Use BIDS-compatible analysis tools like fMRIPrep, MRIQC
   - These tools work directly with BIDS datasets

3. **Version Control Your Configs**
   - Store configuration files in Git
   - Track changes to your conversion procedures
   - Share configs with collaborators

4. **Learn Advanced dcm2bids Features**
   - Custom extractors
   - Advanced search methods
   - Post-processing scripts

---

## 📚 Additional Resources

### Official Documentation
- [dcm2bids Documentation](https://unfmontreal.github.io/Dcm2Bids/)
- [dcm2niix GitHub](https://github.com/rordenlab/dcm2niix)
- [BIDS Specification](https://bids-specification.readthedocs.io/)

### Community Support
- [Neurostars Forum](https://neurostars.org/) - Tag questions with `dcm2bids`
- [dcm2bids GitHub Issues](https://github.com/UNFmontreal/Dcm2Bids/issues)

### Python Virtual Environments
- [Python venv Documentation](https://docs.python.org/3/library/venv.html)
- [Virtual Environments Tutorial](https://realpython.com/python-virtual-environments-a-primer/)

### BIDS Resources
- [BIDS Starter Kit](https://bids-standard.github.io/bids-starter-kit/)
- [BIDS Examples](https://github.com/bids-standard/bids-examples)
- [BIDS Apps](https://bids-apps.neuroimaging.io/)

---

## 🎓 Assessment Questions

Test your understanding:

1. **What is the purpose of using a virtual environment?**
2. **What are the three required options for the dcm2bids command?**
3. **What information do JSON sidecar files contain?**
4. **How do you link fieldmaps to functional data in the config file?**
5. **Where are unpaired files stored after running dcm2bids?**
6. **What is the difference between dcm2niix and dcm2bids?**

---

## 🔧 Appendix A: Quick Reference Commands

### Virtual Environment Management
```bash
# Create environment
python3 -m venv dcm2bids_env

# Activate (macOS/Linux)
source dcm2bids_env/bin/activate

# Activate (Windows)
dcm2bids_env\Scripts\activate

# Deactivate
deactivate

# Delete environment
rm -rf dcm2bids_env
```

### dcm2bids Commands
```bash
# Create BIDS scaffold
dcm2bids_scaffold -o output_directory

# Generate helper files
dcm2bids_helper -d dicom_directory

# Convert to BIDS
dcm2bids -d dicom_dir -p participant_id -c config.json

# With session
dcm2bids -d dicom_dir -p participant_id -s session_id -c config.json

# With auto-extract
dcm2bids -d dicom_dir -p participant_id -c config.json --auto_extract_entities
```

### Package Management
```bash
# Install packages
pip install dcm2niix dcm2bids

# Upgrade packages
pip install --upgrade dcm2bids

# List installed packages
pip list

# Show package info
pip show dcm2bids

# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

---

## 🤝 Acknowledgments

This tutorial is based on the official dcm2bids documentation and tutorial. Special thanks to:
- The dcm2bids development team
- The dcm2niix development team
- The BIDS community

---

**Tutorial Version:** 1.0  
**Last Updated:** November 2025  
**Course:** BIOS 278, Stanford University

**Questions or Issues?**  
Contact your TA or post on the course discussion forum.
