from TLDR.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TLDR.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TLDR.logging import logger

STAGE_NAME = "Stage 01 - Data Ingestion"
try:
  logger.info(f">>> Starting {STAGE_NAME} <<<")
  data_ingestion_pipeline = DataIngestionTrainingPipeline()
  data_ingestion_pipeline.main()
  logger.info(f">>> Completed {STAGE_NAME} <<<")
except Exception as e:
  logger.error(f"Error in {STAGE_NAME}: {e}")
  raise e


STAGE_NAME = "Stage 02 - Data Validation"
try:
  logger.info(f">>> Starting {STAGE_NAME} <<<")
  data_validation_pipeline = DataValidationTrainingPipeline()
  data_validation_pipeline.main()
  logger.info(f">>> Completed {STAGE_NAME} <<<")
except Exception as e:
  logger.error(f"Error in {STAGE_NAME}: {e}")
  raise e

