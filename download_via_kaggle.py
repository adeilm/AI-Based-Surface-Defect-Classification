import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_severstal():
    api = KaggleApi()
    api.authenticate()
    
    competition = "severstal-steel-defect-detection"
    path = "dataset"
    
    print(f"Downloading {competition} to {path}...")
    try:
        api.competition_download_files(competition, path=path)
        print("Download complete! Please unzip the downloaded file.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_severstal()
