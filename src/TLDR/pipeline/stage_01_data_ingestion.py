from TLDR.config.configuration import ConfigurationManager
from TLDR.logging import logger
from TLDR.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:
  def __init__(self) -> None:
    pass
  
  def main(self):
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(config = data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip()
