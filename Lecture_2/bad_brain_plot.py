import nilearn
from nilearn import plotting
import nibabel

# Load the image
img = nibabel.load('/Users/dimuthu/Documents/BIOS_278_mini_course/Lecture_2/sub-0051160_T1w.nii.gz')

# Plot it
plotting.plot_anat(img)
plotting.show()

# Save figure
display = plotting.plot_stat_map(img, threshold=3)
display.savefig('output.png')