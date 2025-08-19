import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        """Fetch data from from the url"""

        try:
            dataset_url=self.config.source_URL
            zip_download_dir=self.config.local_data_file
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id=dataset_url.split("/")[-2]
            prefix="https://drive.google.com/uc?id="
            gdown.download(f"{prefix}{file_id}", zip_download_dir, quiet=False)  # Download the file
            logger.info(f"File downloaded successfully from {dataset_url} into {zip_download_dir}")
        except Exception as e:
            logger.error(f"Error occurred while downloading file: {e}")
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the zip file into the data directory
        returns None
        """
        unzip_path=self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            logger.info(f"Extracting zip file {self.config.local_data_file} into {unzip_path}")
            zip_ref.extractall(unzip_path)
            logger.info(f"Extraction completed. Files are available at {unzip_path}")