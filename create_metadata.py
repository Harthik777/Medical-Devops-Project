import os
import csv

# This path now correctly points to the folder containing the 10 class directories.
dataset_path = 'cerebrovascular_images/cerebrovascular lesions'
output_csv_file = 'medical_images_metadata.csv'

header = ['file_path', 'lesion_type']
print(f"➡️ Generating metadata from '{dataset_path}'...")

try:
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        total_files = 0
        # Loop through each lesion type sub-directory
        for class_name in os.listdir(dataset_path):
            class_path = os.path.join(dataset_path, class_name)
            if os.path.isdir(class_path):
                for filename in os.listdir(class_path):
                    full_path = os.path.join(class_path, filename).replace('\\', '/')
                    writer.writerow([full_path, class_name])
                    total_files += 1
    print(f"✅ Success! Created '{output_csv_file}' with {total_files} entries.")
except FileNotFoundError:
    print(f"❌ Error: The directory '{dataset_path}' was not found. Make sure it's correct.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")