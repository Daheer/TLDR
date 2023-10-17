from TLDR.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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
