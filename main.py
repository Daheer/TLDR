from TLDR.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TLDR.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TLDR.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TLDR.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TLDR.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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

STAGE_NAME = "Stage 03 - Data Transformation"
try:
  logger.info(f">>> Starting {STAGE_NAME} <<<")
  data_transformation_pipeline = DataTransformationTrainingPipeline()
  data_transformation_pipeline.main()
  logger.info(f">>> Completed {STAGE_NAME} <<<")
except Exception as e:
  logger.error(f"Error in {STAGE_NAME}: {e}")
  raise e

STAGE_NAME = "Stage 04 - Model Training"
try:
  logger.info(f">>> Starting {STAGE_NAME} <<<")
  model_trainer_pipeline = ModelTrainerTrainingPipeline()
  model_trainer_pipeline.main()
  logger.info(f">>> Completed {STAGE_NAME} <<<")
except Exception as e:
  logger.error(f"Error in {STAGE_NAME}: {e}")
  raise e

STAGE_NAME = "Stage 05 - Model Evaluation"
try:
  logger.info(f">>> Starting {STAGE_NAME} <<<")
  model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
  model_evaluation_pipeline.main()
  logger.info(f">>> Completed {STAGE_NAME} <<<")
except Exception as e:
  logger.error(f"Error in {STAGE_NAME}: {e}")
  raise e
