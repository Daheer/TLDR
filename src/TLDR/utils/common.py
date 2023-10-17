import os
from box.exceptions import BoxValueError
import yaml
from TLDR.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
  """
  Read a yaml file and return a ConfigBox object.
  """
  try:
    with open(path_to_yaml, "r") as yaml_file:
      yaml_dict = yaml.safe_load(yaml_file)
      logger.info(f"yaml file: {yaml_file} read successfully.")
      return ConfigBox(yaml_dict)
  except BoxValueError:
    raise ValueError(f"Error reading yaml file at {path_to_yaml}.")
    logger.error(f"Error reading yaml file at {path_to_yaml}.")
  except Exception as e:
    raise e
    logger.error(f"Error reading yaml file at {path_to_yaml}.")

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
  """
  Create directories if they don't exist.
  """
  for path in path_to_directories:
    os.makedirs(path, exist_ok=True)
    if verbose:
      logger.info(f"Created directory: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
  """
  Get the size of a file or directory in KB.
  """
  size = round(os.path.getsize(path) / 1024)
  return f"~{size} KB"
