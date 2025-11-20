# BIOS 278: Reproducibility and Data Science in Computational Brain Image Analysis

<div align="center">

![Stanford University](https://img.shields.io/badge/Stanford-University-8C1515?style=for-the-badge&logo=stanford&logoColor=white)
![Course](https://img.shields.io/badge/Course-BIOS%20278-B83A4B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**🧠 Advancing Reproducible Neuroimaging Research 🧠**

</div>

---

## 📋 Course Overview

Welcome to **BIOS 278**! This course provides hands-on training in modern computational approaches for brain imaging analysis, with a strong emphasis on reproducibility, standardization, and scalable computing practices.

### 🎯 Learning Goals

By the end of this course, students will be able to:

- ✅ Organize neuroimaging data using international standards (BIDS)
- ✅ Implement version control for code and data using Git/GitHub
- ✅ Create reproducible computational environments with containers
- ✅ Deploy analyses on high-performance computing (HPC) systems
- ✅ Apply best practices for open and reproducible neuroscience

---

## 📚 Course Structure

This repository contains materials for three comprehensive laboratory sessions:

<table>
<tr>
<td width="33%" align="center">

### 🔰 Lab 1
**GitHub & BIDS**

📦 Version Control  
🗂️ Data Organization  
✓ Standards & Validation

</td>
<td width="33%" align="center">

### 🐳 Lab 2
**Containers**

🐋 Docker  
📦 Singularity  
🔒 Reproducible Environments

</td>
<td width="33%" align="center">

### 🚀 Lab 3
**High-Performance Computing**

⚡ HPC Clusters  
📊 Parallel Processing  
🔄 Batch Job Submission

</td>
</tr>
</table>

---

## 🔬 Lab Details

### Lab 1: Introduction to GitHub and BIDS Standard

<details>
<summary><b>🔍 Click to expand Lab 1 details</b></summary>

<br>

**Objective:** Learn version control and data standardization for neuroimaging research

#### Topics Covered:
- 📥 **Git Fundamentals**
  - Cloning repositories
  - Creating and managing repositories
  - Committing and pushing changes
  
- 🧠 **BIDS (Brain Imaging Data Structure)**
  - Understanding BIDS principles
  - Manual data reorganization
  - Creating dataset metadata (`dataset_description.json`)
  - Validating datasets with BIDS validator

#### Key Skills:
```bash
✓ git clone / git add / git commit / git push
✓ BIDS directory structure
✓ JSON metadata files
✓ Online BIDS validation
```

#### Prerequisites:
- Git installed on your system
- GitHub account
- Text editor (VS Code, Sublime, etc.)

#### Resources:
- [BIDS Specification](https://bids-specification.readthedocs.io/)
- [Git Documentation](https://git-scm.com/doc)
- [BIDS Validator](https://bids-standard.github.io/bids-validator/)

</details>

---

### Lab 2: Container Technologies (Docker & Singularity)

<details>
<summary><b>🔍 Click to expand Lab 2 details</b></summary>

<br>

**Objective:** Master containerization for reproducible computational environments

#### Topics Covered:
- 🐳 **Docker Fundamentals**
  - Understanding container concepts
  - Pulling and running Docker images
  - Building custom Docker images
  - Creating Dockerfiles for neuroimaging pipelines
  - Managing container storage and networking

- 📦 **Singularity for HPC**
  - Why Singularity for research computing
  - Converting Docker images to Singularity
  - Running Singularity containers
  - Building Singularity definition files
  - Singularity on shared HPC systems

- 🔬 **Neuroimaging Containers**
  - Using pre-built neuroimaging containers (FSL, FreeSurfer, ANTS)
  - BIDS Apps framework
  - Reproducible analysis pipelines

#### Key Skills:
```bash
# Docker
✓ docker pull / docker run / docker build
✓ Dockerfile creation
✓ Container data mounting

# Singularity  
✓ singularity pull / singularity run / singularity build
✓ Definition file creation
✓ Docker-to-Singularity conversion
```

#### Prerequisites:
- Completed Lab 1
- Docker Desktop installed (for Docker section)
- Access to Singularity (on HPC system or local install)

#### Resources:
- [Docker Documentation](https://docs.docker.com/)
- [Singularity Documentation](https://sylabs.io/docs/)
- [BIDS Apps](https://bids-apps.neuroimaging.io/)
- [Neurodocker](https://github.com/ReproNim/neurodocker)

#### Example Containers:
| Tool | Docker Hub | Purpose |
|------|------------|---------|
| FSL | `brainlife/fsl` | Structural & functional MRI |
| FreeSurfer | `freesurfer/freesurfer` | Cortical surface analysis |
| ANTS | `antsx/ants` | Image registration |
| fMRIPrep | `nipreps/fmriprep` | fMRI preprocessing pipeline |

</details>

---

### Lab 3: High-Performance Computing (HPC)

<details>
<summary><b>🔍 Click to expand Lab 3 details</b></summary>

<br>

**Objective:** Deploy scalable neuroimaging analyses on HPC clusters

#### Topics Covered:
- 🖥️ **HPC Fundamentals**
  - Understanding cluster architecture
  - SSH and remote access
  - File systems and storage (home, scratch, group)
  - Module systems and software management

- 📊 **Job Scheduling with SLURM**
  - Writing SLURM submission scripts
  - Resource allocation (CPUs, memory, time)
  - Job arrays for parallel processing
  - Monitoring and managing jobs
  - Dependencies and workflows

- ⚡ **Parallel Processing**
  - Embarrassingly parallel problems
  - Processing multiple subjects simultaneously
  - GNU Parallel for task distribution
  - Array jobs for batch processing

- 🔄 **Neuroimaging Workflows on HPC**
  - Running containerized pipelines (Singularity)
  - Data transfer strategies
  - Debugging failed jobs
  - Optimization and best practices

#### Key Skills:
```bash
# HPC Access
✓ ssh / scp / rsync
✓ module load / module list

# SLURM
✓ sbatch / squeue / scancel
✓ Job arrays
✓ Resource requests
✓ Parallel job submission

# Workflow Management
✓ Shell scripting
✓ GNU Parallel
✓ Job dependencies
```

#### Prerequisites:
- Completed Labs 1 & 2
- Access to HPC cluster (e.g., Stanford Sherlock, farmshare)
- SSH client
- Basic Linux/Unix command line skills

#### Resources:
- [SLURM Documentation](https://slurm.schedmd.com/)
- [Stanford Sherlock Documentation](https://www.sherlock.stanford.edu/docs/)
- [GNU Parallel Tutorial](https://www.gnu.org/software/parallel/parallel_tutorial.html)
- [Best Practices for HPC](https://hpc-wiki.info/hpc/Best_Practices)

#### Example SLURM Script:
```bash
#!/bin/bash
#SBATCH --job-name=fmriprep
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=32GB
#SBATCH --array=1-20

# Load modules or containers
# Process subject ${SLURM_ARRAY_TASK_ID}
```

</details>

---

## 🛠️ Required Software

### All Labs
- **Git** (version control)
- **Text Editor** (VS Code, Sublime Text, Atom, etc.)
- **Terminal/Shell** access

### Lab 1 Specific
- GitHub account
- BIDS validator (online or desktop)

### Lab 2 Specific
- **Docker Desktop** ([Download](https://www.docker.com/products/docker-desktop/))
  - Windows 10/11 Pro, macOS, or Linux
- **Singularity/Apptainer** (typically on HPC)
  - Installation instructions: [Sylabs.io](https://sylabs.io/guides/latest/user-guide/)

### Lab 3 Specific
- **HPC Cluster Access** (Stanford Sherlock or farmshare)
- **SSH Client**
  - macOS/Linux: Built-in terminal
  - Windows: PuTTY, MobaXterm, or Windows Terminal

---

## 🚀 Getting Started

### 1️⃣ Clone This Repository

```bash
# Navigate to your desired directory
cd ~/Documents

# Clone the repository
git clone https://github.com/DimuthuHemachandra/BIOS_278.git

# Enter the directory
cd BIOS_278

# Explore the contents
ls -la
```

### 2️⃣ Set Up Your Environment

Follow the installation guides in each lab folder to ensure you have the required software.

### 3️⃣ Complete the Labs

Work through each lab in order, as they build upon each other:
1. Lab 1: GitHub & BIDS (Foundation)
2. Lab 2: Containers (Reproducibility)
3. Lab 3: HPC (Scalability)

---

## 📖 Additional Resources

### Neuroimaging Standards
- 🔗 [BIDS - Brain Imaging Data Structure](https://bids.neuroimaging.io/)
- 🔗 [NIDM - Neuroimaging Data Model](http://nidm.nidash.org/)
- 🔗 [OpenNeuro - Open neuroimaging datasets](https://openneuro.org/)

### Reproducibility Tools
- 🔗 [ReproNim - Reproducible Neuroimaging](https://www.repronim.org/)
- 🔗 [Datalad - Data management](https://www.datalad.org/)
- 🔗 [Neurodocker - Neuroimaging containers](https://github.com/ReproNim/neurodocker)

### Neuroimaging Software
- 🔗 [FSL - FMRIB Software Library](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)
- 🔗 [FreeSurfer - Cortical surface analysis](https://surfer.nmr.mgh.harvard.edu/)
- 🔗 [AFNI - Analysis of Functional NeuroImages](https://afni.nimh.nih.gov/)
- 🔗 [SPM - Statistical Parametric Mapping](https://www.fil.ion.ucl.ac.uk/spm/)
- 🔗 [ANTS - Advanced Normalization Tools](http://stnava.github.io/ANTs/)

### Computing Resources
- 🔗 [Stanford Sherlock Cluster](https://www.sherlock.stanford.edu/)
- 🔗 [Stanford Research Computing Center](https://srcc.stanford.edu/)
- 🔗 [Software Carpentry](https://software-carpentry.org/)

---

## 💡 Tips for Success

### 🎯 Best Practices

1. **📝 Document Everything**
   - Keep detailed notes of commands and processes
   - Comment your code and scripts
   - Maintain a lab notebook (digital or physical)

2. **🔄 Version Control Regularly**
   - Commit changes frequently with meaningful messages
   - Push to GitHub after completing major steps
   - Use branches for experimental work

3. **🧪 Test on Small Datasets First**
   - Validate your pipeline before scaling up
   - Use small samples to debug quickly
   - Check outputs at each processing stage

4. **🤝 Collaborate and Share**
   - Help your classmates
   - Share useful resources you find
   - Contribute to discussions

5. **🆘 Ask for Help**
   - Consult documentation first
   - Search for error messages online
   - Reach out to instructors and TAs
   - Use course discussion forums

---

## 🏆 Learning Outcomes

Upon completing all three labs, you will have:

✨ **Technical Skills**
- Proficiency in Git/GitHub for version control
- Ability to organize neuroimaging data using BIDS
- Experience building and running Docker and Singularity containers
- Competence in submitting and managing HPC jobs
- Understanding of parallel processing concepts

✨ **Research Skills**
- Implementing reproducible analysis workflows
- Creating shareable computational environments
- Scaling analyses to large datasets
- Debugging computational pipelines
- Following best practices for open science

✨ **Professional Skills**
- Collaboration using version control
- Technical documentation
- Problem-solving in computational environments
- Resource management and optimization

---

## 📧 Contact and Support

### Course Instructor
**Dimuthu Hemachandra, PhD**  
Stanford University

### Getting Help

1. **📚 Check the Documentation**
   - Lab instructions in each folder
   - Resource links provided above

2. **💬 Discussion Forum**
   - Post questions on Canvas/Ed Discussion
   - Help your classmates

3. **👥 Office Hours**
   - Check course syllabus for times
   - Come prepared with specific questions

4. **🐛 Report Issues**
   - Found a bug in the lab materials?
   - Open an issue on this GitHub repository

---

## 🤝 Contributing

We welcome contributions to improve the course materials!

### How to Contribute:
1. Fork this repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit with clear messages (`git commit -m 'Add helpful example'`)
5. Push to your branch (`git push origin feature/improvement`)
6. Open a Pull Request

### What to Contribute:
- Bug fixes in lab instructions
- Additional examples or tutorials
- Improved documentation
- Resource links
- Troubleshooting tips

---

## 📜 License

This course material is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit

---

## 🙏 Acknowledgments

This course builds upon the excellent work of:
- The BIDS community for neuroimaging standardization
- The ReproNim project for reproducible neuroimaging tools
- The Neuroimaging community for open-source software
- Stanford Research Computing for HPC infrastructure and support

Special thanks to all students and TAs who have contributed feedback and improvements to these materials.

---

<div align="center">

### 🌟 Star this repository if you find it helpful! 🌟

![Brain](https://img.shields.io/badge/Made%20with-🧠-lightgrey?style=for-the-badge)
![Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)

**Happy Learning! 🚀**

</div>

---

## 📅 Course Timeline

| Week | Lab | Topic | Deliverable |
|------|-----|-------|-------------|
| 1-2 | Lab 1 | GitHub & BIDS | BIDS-formatted repository |
| 3-4 | Lab 2 | Containers | Custom Docker/Singularity image |
| 5-6 | Lab 3 | HPC Computing | Batch processing results |

---

## 🔖 Quick Links

| Resource | Link |
|----------|------|
| Course Repository | [github.com/DimuthuHemachandra/BIOS_278](https://github.com/DimuthuHemachandra/BIOS_278) |
| BIDS Validator | [bids-standard.github.io/bids-validator](https://bids-standard.github.io/bids-validator/) |
| Docker Hub | [hub.docker.com](https://hub.docker.com) |
| Singularity Hub | [singularity-hub.org](https://singularity-hub.org) |
| Stanford Sherlock | [sherlock.stanford.edu](https://www.sherlock.stanford.edu/) |
| Stanford Sherlock Ondemand| [sherlock.ondemand](https://ondemand.sherlock.stanford.edu/pun/sys/dashboard/) |
| Stanford Farmshare Ondemand| [farmshare.ondemand](https://ondemand-01.farmshare.stanford.edu/pun/sys/dashboard) |

---

**Last Updated:** November 2025  
**Course Website:** [Link to course website if applicable]  
**GitHub Repository:** https://github.com/DimuthuHemachandra/BIOS_278
