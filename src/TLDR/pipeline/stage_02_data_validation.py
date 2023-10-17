from TLDR.config.configuration import ConfigurationManager
from TLDR.logging import logger
from TLDR.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
  def __init__(self) -> None:
    pass
  
  def main(self):
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(data_validation_config)
    data_validation.validate_all_files_exist()