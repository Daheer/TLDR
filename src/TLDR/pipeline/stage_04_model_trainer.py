from TLDR.config.configuration import ConfigurationManager
from TLDR.logging import logger
from TLDR.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    model_trainer = ModelTrainer(model_trainer_config)
    model_trainer.train()