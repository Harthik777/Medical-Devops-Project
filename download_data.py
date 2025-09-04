import kaggle

# The corrected dataset slug you are using
dataset_slug = 'buraktaci/cerebrovascular-lesions'
# The folder where the script will save the data
download_path = 'cerebrovascular_images'

print("➡️ Authenticating and downloading image dataset...")
try:
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(
        dataset_slug,
        path=download_path,
        unzip=True
    )
    print(f"✅ Download complete. Images are in '{download_path}'.")
except Exception as e:
    print(f"❌ Error downloading data: {e}")