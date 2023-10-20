from TLDR.config.configuration import ConfigurationManager
from TLDR.logging import logger
from TLDR.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evaluation_config()
    model_evaluation = ModelEvaluation(model_evaluation_config)
    model_evaluation.evaluate()