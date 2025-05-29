"""
Utility functions for creating and managing YOLO format datasets.
Provides functionality for splitting datasets, creating directory structures,
copying dataset contents, and generating YOLO configuration files.

Functions:
---------
split_images
    Calculates and returns the dataset splits for training, testing and validation.

    Args:
        train_ratio (float): Ratio of images to use for training (0.0-1.0)
        test_ratio (float): Ratio of images to use for testing (0.0-1.0)
        val_ratio (float): Ratio of images to use for validation (0.0-1.0)
        images_path (Path): Directory containing the source images
        labels_path (Path): Directory containing the YOLO format labels
        seed (int, optional): Random seed for reproducibility. Defaults to 59

    Returns:
        dict[str, list[Path]]: Dictionary containing file paths for each split
        Example: {
            'train': [Path('image1.jpg'), ...],
            'test': [Path('image2.jpg'), ...],
            'val': [Path('image3.jpg'), ...]
        }

create_dataset_paths
    Creates the required directory structure for a YOLO dataset.

    Args:
        sub_paths (list[str], optional): Subdirectories to create under each split.
            Defaults to ["images", "labels"]
        splits (list[str], optional): Dataset split types.
            Defaults to ["train", "test", "val"]

    Returns:
        None

    Raises:
        OSError: If directory creation fails

copy_dataset_contents
    Copies images and labels to their respective directories based on the splits.

    Args:
        dataset_path (Path): Root directory of the dataset
        labels_path (Path): Source directory containing the labels
        splits (dict[str, list[Path]]): Dictionary containing file paths for each split
            as returned by split_images()

    Returns:
        None

    Raises:
        FileNotFoundError: If source files are not found
        OSError: If copy operation fails

create_yolo_yaml
    Creates a YAML configuration file for YOLO training.

    Args:
        dataset_path (Path): Root directory of the dataset
        classes (list[str]): List of class names in the dataset

    Returns:
        None

    Raises:
        OSError: If YAML file creation fails

Examples:
--------
>>> from pathlib import Path
>>> from dataset_utils import split_images, create_dataset_paths
>>> 
>>> # Split dataset
>>> splits = split_images(0.8, 0.1, 0.1, 
...                      Path('images'), 
...                      Path('labels'))
>>> 
>>> # Create directory structure
>>> create_dataset_paths()
"""

from .directory_utils import split_images, create_dataset_paths, copy_dataset_contents
from .file_utils import create_yolo_yaml, read_classes
from .logger_utils import create_logger, add_run_separator, logger

__version__ = "0.1"
__author__ = "Tarik Eren Tosun"

__all__ = [
    # Directory utils
    "split_images",
    "create_dataset_paths",
    "copy_dataset_contents",

    # File utils
    "create_yolo_yaml",
    "read_classes",

    # Logger utils
    "create_logger",
    "add_run_separator"
]

