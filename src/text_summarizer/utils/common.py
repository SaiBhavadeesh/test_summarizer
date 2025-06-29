import os
import yaml
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.text_summarizer.logging import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
    
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    
    Raises:
        ValueError: If the file does not exist or is not a valid YAML file.
    """
    try:
        if not os.path.exists(path_to_yaml):
            raise ValueError(f"File {path_to_yaml} does not exist.")
        
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    
    except BoxValueError as e:
        raise ValueError(f"Invalid YAML file: {path_to_yaml}") from e
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(paths: list, verbose: bool = True):
    """
    Creates directories if they do not exist.
    
    Args:
        paths (list): List of directory paths to create.
    
    Returns:
        None
    """
    for path in paths:
        path = Path(path)
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory {path} created successfully.")
        except Exception as e:
            raise e
