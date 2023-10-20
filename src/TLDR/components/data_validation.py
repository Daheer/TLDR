import os
from TLDR.logging import logger
from TLDR.entity import DataValidationConfig

class DataValidation:
  def __init__(self, config: DataValidationConfig):
    self.config = config

  def validate_all_files_exist(self) -> bool:
    try:
      validation_status = None
      all_existing_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'samsum_dataset'))
      for file in self.config.ALL_REQUIRED_FILES:
        if file in all_existing_files:
          validation_status = True
          logger.info(f'Validation Status for {file}: {validation_status}')
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f'Validation Status: {validation_status}')
        else:
          validation_status = False
          logger.info(f'Validation Status for {file}: {validation_status}')
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f'Validation Status: {validation_status}')
    except Exception as e:
      raise e