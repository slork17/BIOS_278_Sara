# Lab 1: Introduction to GitHub and BIDS Standard

**Course:** BIOS 278 - Reproducibility and Data Science in Computational Brain Image Analysis  
**Stanford University**

---

## Learning Objectives

By the end of this lab, you will be able to:
1. Clone an existing GitHub repository
2. Create your own GitHub repository
3. Understand and apply the BIDS (Brain Imaging Data Structure) standard
4. Create a valid `dataset_description.json` file
5. Validate your BIDS dataset using the online BIDS validator
6. Push changes to your GitHub repository

---

## Prerequisites

- GitHub account (create one at https://github.com if you don't have one)
- Git installed on your computer
  - Check by running: `git --version`
  - If not installed, download from: https://git-scm.com/downloads
- Text editor (VS Code, Sublime Text, or any editor of your choice)

---

## Part 1: Cloning the Course Repository

### What is Cloning?

Cloning creates a local copy of a remote repository on your computer, including all files, commit history, and branches.

### Steps to Clone

1. **Open your terminal** (macOS/Linux) or **Git Bash** (Windows)

2. **Navigate to your desired directory:**
   ```bash
   cd ~/Documents  # or wherever you want to store the repository
   ```

3. **Clone the course repository:**
   ```bash
   git clone https://github.com/DimuthuHemachandra/BIOS_278.git
   ```

4. **Navigate into the cloned repository:**
   ```bash
   cd BIOS_278
   ```

5. **Explore the repository contents:**
   ```bash
   ls -la  # List all files including hidden ones
   ```

6. **Locate the MRI data folder** and examine its current structure

---

## Part 2: Creating Your Own GitHub Repository

### Steps to Create a New Repository

1. **Go to GitHub** and sign in to your account

2. **Click the "+" icon** in the top right corner and select "New repository"

3. **Configure your repository:**
   - **Repository name:** `BIOS278_Lab1_[YourName]` (e.g., `BIOS278_Lab1_JohnDoe`)
   - **Description:** "BIDS-formatted MRI dataset for BIOS 278 Lab 1"
   - **Visibility:** Choose Public or Private (recommend Public for this course)
   - **Initialize repository:** Check "Add a README file"
   - Leave other options unchecked for now

4. **Click "Create repository"**

5. **Clone your new repository to your local machine:**
   ```bash
   cd ~/Documents  # Navigate back to your Documents folder
   git clone https://github.com/[YourUsername]/BIOS278_Lab1_[YourName].git
   cd BIOS278_Lab1_[YourName]
   ```

---

## Part 3: Understanding BIDS Standard

### What is BIDS?

**Brain Imaging Data Structure (BIDS)** is a standardized way to organize and describe neuroimaging and behavioral data. It makes data:
- **Easier to share** with collaborators
- **Machine-readable** for automated analysis
- **Reproducible** across different labs and software tools

### BIDS Directory Structure

A basic BIDS dataset follows this structure:

```
my_dataset/
├── dataset_description.json
├── participants.tsv
├── participants.json (optional)
├── README
├── CHANGES
└── sub-<label>/
    └── ses-<label>/  (optional, if multiple sessions)
        └── anat/
            ├── sub-<label>_ses-<label>_T1w.nii.gz
            └── sub-<label>_ses-<label>_T1w.json
        └── func/
            ├── sub-<label>_ses-<label>_task-<label>_bold.nii.gz
            └── sub-<label>_ses-<label>_task-<label>_bold.json
```

### Key BIDS Principles

1. **Consistent naming:** Files follow a strict naming convention with key-value pairs
2. **Metadata files:** Each imaging file should have an accompanying JSON sidecar
3. **Dataset descriptor:** The `dataset_description.json` is required at the root
4. **Hierarchical organization:** Data organized by subject, session, and modality

---

## Part 4: Copying and Reorganizing Data to BIDS Format

### Step 4.1: Copy MRI Data

1. **Copy the MRI data** from the cloned course repository to your new repository:
   ```bash
   cp -r ~/Documents/BIOS_278/[path_to_mri_data] ~/Documents/BIOS278_Lab1_[YourName]/
   ```

### Step 4.2: Create BIDS Directory Structure

2. **Create the basic BIDS folder structure:**
   ```bash
   cd ~/Documents/BIOS278_Lab1_[YourName]
   mkdir -p sub-01/anat
   mkdir -p sub-01/func
   ```

   If you have multiple subjects, repeat for each:
   ```bash
   mkdir -p sub-02/anat
   mkdir -p sub-02/func
   ```

### Step 4.3: Rename and Move Files

3. **Rename and move your imaging files** following BIDS conventions:

   For anatomical data:
   ```bash
   mv [original_file].nii.gz sub-01/anat/sub-01_T1w.nii.gz
   ```

   For functional data:
   ```bash
   mv [original_functional_file].nii.gz sub-01/func/sub-01_task-rest_bold.nii.gz
   ```

   **Important naming conventions:**
   - Subject ID: `sub-<label>` (e.g., `sub-01`, `sub-pilot1`)
   - Session: `ses-<label>` (if applicable)
   - Anatomical: `_T1w`, `_T2w`, `_FLAIR`, etc.
   - Functional: `_task-<label>_bold` (e.g., `_task-rest_bold`, `_task-nback_bold`)

### Step 4.4: Create JSON Sidecar Files

4. **Create metadata JSON files** for each imaging file. For example, create `sub-01_T1w.json`:
   
   ```bash
   cd sub-01/anat
   nano sub-01_T1w.json  # or use your preferred text editor
   ```

   Add the following content (adjust values based on your actual data):
   ```json
   {
       "Modality": "MR",
       "MagneticFieldStrength": 3,
       "Manufacturer": "Siemens",
       "ManufacturersModelName": "Prisma",
       "EchoTime": 0.00456,
       "RepetitionTime": 2.3,
       "FlipAngle": 8
   }
   ```

---

## Part 5: Creating dataset_description.json

### What is dataset_description.json?

This is a **required file** at the root of every BIDS dataset. It provides essential metadata about the dataset, including its name, authors, and BIDS version.

### Creating the File

1. **Navigate to your repository root:**
   ```bash
   cd ~/Documents/BIOS278_Lab1_[YourName]
   ```

2. **Create and edit the file:**
   ```bash
   nano dataset_description.json
   ```

3. **Add the following content** (customize with your information):

   ```json
   {
       "Name": "BIOS 278 Lab 1 Dataset",
       "BIDSVersion": "1.9.0",
       "DatasetType": "raw",
       "License": "CC0",
       "Authors": [
           "Your Name",
           "Your Partner's Name (if applicable)"
       ],
       "Acknowledgements": "Data provided by BIOS 278 course",
       "HowToAcknowledge": "Please cite this paper: [reference if applicable]",
       "Funding": [
           "Stanford University"
       ],
       "ReferencesAndLinks": [
           "https://github.com/DimuthuHemachandra/BIOS_278"
       ],
       "DatasetDOI": ""
   }
   ```

### Required Fields

- **Name:** A descriptive name for your dataset
- **BIDSVersion:** The version of BIDS standard you're following (currently 1.9.0)
- **DatasetType:** Usually "raw" for original data

### Optional but Recommended Fields

- **License:** How others can use your data (e.g., CC0, CC-BY-4.0)
- **Authors:** List of people who contributed to the dataset
- **Acknowledgements:** Recognition of contributions or support
- **Funding:** Funding sources

4. **Save the file** (Ctrl+O, Enter, Ctrl+X in nano)

---

## Part 6: Validating Your BIDS Dataset

### Why Validate?

The BIDS validator checks that your dataset follows the BIDS specification correctly. This ensures compatibility with BIDS-compatible analysis tools.

### Using the Online BIDS Validator

1. **Go to the BIDS Validator website:**
   https://bids-standard.github.io/bids-validator/

2. **Select your dataset folder:**
   - Click "Select Dataset"
   - Navigate to your `BIOS278_Lab1_[YourName]` folder
   - Select the entire folder

3. **Review validation results:**
   - **Green checks (✓):** Your dataset passed these checks
   - **Warnings (⚠️):** Non-critical issues that should be addressed
   - **Errors (✗):** Critical issues that must be fixed

4. **Fix any errors or warnings:**
   - Read the error messages carefully
   - Common issues:
     - Missing required files (e.g., `dataset_description.json`)
     - Incorrect file naming
     - Missing JSON sidecars
     - Invalid JSON syntax

5. **Re-validate** until you have no errors

### Common Validation Errors and Fixes

| Error | Solution |
|-------|----------|
| Missing `dataset_description.json` | Create the file at the root directory |
| Invalid JSON syntax | Check for missing commas, brackets, or quotes |
| Incorrect file naming | Ensure files follow BIDS naming conventions |
| Missing participants.tsv | Create a basic participants file (see below) |

### Creating participants.tsv (if needed)

```bash
cd ~/Documents/BIOS278_Lab1_[YourName]
nano participants.tsv
```

Add this content:
```
participant_id	age	sex
sub-01	25	M
sub-02	28	F
```

**Note:** Use actual tabs (not spaces) between columns in TSV files.

---

## Part 7: Pushing Changes to GitHub

### Understanding Git Workflow

The basic Git workflow consists of:
1. **Add:** Stage changes for commit
2. **Commit:** Save changes with a descriptive message
3. **Push:** Upload commits to GitHub

### Steps to Push Your Changes

1. **Check the status of your repository:**
   ```bash
   cd ~/Documents/BIOS278_Lab1_[YourName]
   git status
   ```
   This shows which files have been modified, added, or are untracked.

2. **Add all your changes:**
   ```bash
   git add .
   ```
   The `.` adds all changes. Alternatively, add specific files:
   ```bash
   git add dataset_description.json sub-01/
   ```

3. **Commit your changes with a descriptive message:**
   ```bash
   git commit -m "Add BIDS-formatted MRI data and dataset description"
   ```

4. **Push to GitHub:**
   ```bash
   git push origin main
   ```
   
   If you're using an older repository, the default branch might be `master`:
   ```bash
   git push origin master
   ```

5. **Verify on GitHub:**
   - Go to your repository on GitHub
   - Refresh the page
   - Confirm all your files are visible

### Useful Git Commands

```bash
# View commit history
git log

# See differences in modified files
git diff

# Undo changes to a file (before staging)
git checkout -- filename

# Remove file from staging (after git add)
git reset filename

# View remote repository URL
git remote -v
```

---

## Part 8: Best Practices and Tips

### Git Best Practices

1. **Commit often** with clear, descriptive messages
2. **Don't commit large files** (>100MB) - use Git LFS if needed
3. **Write meaningful commit messages:**
   - Good: "Add T1w anatomical scan for sub-01"
   - Bad: "Update files"
4. **Pull before you push** if working with collaborators: `git pull origin main`

### BIDS Best Practices

1. **Use consistent naming** across all subjects
2. **Include metadata** in JSON sidecars
3. **Document your dataset** in the README file
4. **Validate early and often** to catch errors quickly
5. **Follow the principle of least surprise** - organize data logically

### Troubleshooting

**Problem:** `git push` is rejected  
**Solution:** Pull first with `git pull origin main`, then push again

**Problem:** BIDS validator shows encoding errors  
**Solution:** Ensure TSV files use tab characters, not spaces

**Problem:** Can't find `.git` folder  
**Solution:** This is a hidden folder. Use `ls -la` to see it

---

## Deliverables

Submit the following by the end of the lab:

1. **GitHub repository URL** containing your BIDS-formatted dataset
2. **Screenshot** of the BIDS validator showing no errors
3. **Brief report** (1-2 paragraphs) answering:
   - What challenges did you encounter while reformatting to BIDS?
   - Why is standardization important for neuroimaging research?

---

## Additional Resources

### BIDS
- [BIDS Specification](https://bids-specification.readthedocs.io/)
- [BIDS Starter Kit](https://bids-standard.github.io/bids-starter-kit/)
- [BIDS Examples](https://github.com/bids-standard/bids-examples)

### Git and GitHub
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Learn Git Branching (Interactive Tutorial)](https://learngitbranching.js.org/)

### Tools
- [BIDS Validator (Desktop App)](https://github.com/bids-standard/bids-validator)
- [PyBIDS - BIDS in Python](https://bids-standard.github.io/pybids/)
- [dcm2bids - Convert DICOM to BIDS](https://unfmontreal.github.io/Dcm2Bids/)

---

## Questions and Help

If you encounter issues:
1. Check the error messages carefully
2. Consult the BIDS specification
3. Ask your peers or TAs
4. Post on the course discussion forum

**Good luck with your first lab!**
