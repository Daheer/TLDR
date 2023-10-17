import os
import urllib.request as request
import zipfile
from TLDR.logging import logger
from TLDR.utils.common import get_size
from TLDR.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.config = config

  def download_file(self):
    if not os.path.exists(self.config.local_data_file):
      filename, headers = request.urlretrieve(
        url = self.config.source_URL,
        filename = self.config.local_data_file
      )
      logger.info(f"Downloaded {filename} with info \n{headers}")
    else:
      logger.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}")

  def extract_zip(self):
    unzip_dir = self.config.unzip_dir
    logger.info(f"Extracting {self.config.local_data_file} to {unzip_dir}")
    os.makedirs(unzip_dir, exist_ok=True)
    with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
      zip_ref.extractall(unzip_dir)
    logger.info(f"Done extracting {self.config.local_data_file} to {self.config.unzip_dir}")