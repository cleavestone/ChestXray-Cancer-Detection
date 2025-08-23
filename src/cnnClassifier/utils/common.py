import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from base64 import b64decode, b64encode

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty

    Returns:
        ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yaml,"r") as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ create list of directories

    Args:
        path_to_directories (list): list of directories to be created
        verbose (bool, optional): if True, prints the directories being created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data:dict):
    """saves data to json file
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file

    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """ loads data from a json file

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributors
    """
    with open(path,'r') as f:
        content=json.laod(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)   

@ensure_annotations
def save_bin(path:Path, data:Any):
    """saves data to a binary file
    
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """Loads data from a binary file"""
    data=joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """Gets the size of a file or directory
    
    Args:
        path (Path): path to file or directory
        
    Returns:
        str: size of the file or directory in human-readable format
    """
    size_in_kb=os.path.getsize(path)/1024
    return f"{size_in_kb:.2f} KB" if size_in_kb < 1024 else f"{size_in_kb/1024:.2f} MB"

def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


