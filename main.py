import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('buraktaci/cerebrovascular-lesions', path='.', unzip=True)

