import os
import subprocess

# Set Windows-mapped paths
input_root = "/mnt/c/Users/rushi/compNeuroAD/adEarly/ADNI"
output_root = "/mnt/c/Users/rushi/compNeuroAD/adEarly/NIFTI_ADNI"

os.makedirs(output_root, exist_ok=True)

for patient_id in os.listdir(input_root):
    patient_path = os.path.join(input_root, patient_id)
    if not os.path.isdir(patient_path):
        continue

    for root, dirs, files in os.walk(patient_path):
        if any(f.endswith('.dcm') for f in files):
            # Output folder per patient
            out_folder = os.path.join(output_root, patient_id)
            os.makedirs(out_folder, exist_ok=True)

            print(f"Converting DICOM series in: {root}")
            subprocess.run([
                "dcm2niix",
                "-z", "y",          # Compress output
                "-o", out_folder,   # Output folder
                "-f", "%p_%s",      # Filename pattern: protocol_series
                root                # Input DICOM folder
            ])
