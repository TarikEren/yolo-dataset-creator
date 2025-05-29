# TODO: Requires testing

import os
import sys

# Add the script's directory to Python's path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)

import argparse

from pathlib import Path
from typing import Optional

from utils import (split_images, 
                   create_dataset_paths,
                   copy_dataset_contents,
                   create_yolo_yaml,
                   create_logger,
                   add_run_separator,
                   read_classes)

# Create the logger and add a new run separator
logger = create_logger()
logger.info(add_run_separator())

def main(train_ratio: float,
         test_ratio: float,
         val_ratio: float,
         images: str = "./images",
         labels: str = "./labels",
         dataset: str = "./dataset",
         class_file_path: str = "./classes"):
    """
    Creates a YOLO dataset structure from images and labels, splitting them into train, test and validation sets.
        Args:
            train_ratio (float): Ratio of images to use for training (between 0 and 1)
            test_ratio (float): Ratio of images to use for testing (between 0 and 1)
            val_ratio (float): Ratio of images to use for validation (between 0 and 1)
            images (str, optional): Path to the directory containing images. Defaults to "./images"
            labels (str, optional): Path to the directory containing labels. Defaults to "./labels"
            dataset (str, optional): Path where the dataset will be created. Defaults to "./dataset"
            class_file_path (str, optional): Path to the file containing class names. Defaults to "./classes"
        Note:
            The sum of train_ratio, test_ratio, and val_ratio should be 1.0
            Images and labels should have matching filenames (only different extensions)
            Class file should contain one class name per line
        Returns:
            None: Creates dataset directory structure with train, test, val splits and yaml configuration
    """

    # Required paths
    images_path = Path(images)
    labels_path = Path(labels)
    dataset_path = Path(dataset)

    # Checking if ratios are valid (Not none and sum should be 1)
    ratios = {
        "Train": train_ratio,
        "Test": test_ratio,
        "Val": val_ratio
    }    
    ratio_sum = 0
    for key, ratio in ratios.items():
        if ratio is None:
            logger.error(f"{key} ratio is None")
            raise ValueError(f"{key} ratio is None")
        ratio_sum += ratio

    if ratio_sum != 1:
        logger.error(f"Sum of train, test and val ratios ({val_ratio}) is not equal to 1")
        raise ValueError(f"Sum of train, test and val ratios ({val_ratio}) is not equal to 1")

    classes = read_classes(class_file=class_file_path)

    splits = split_images(train_ratio=train_ratio,
                        test_ratio=test_ratio,
                        val_ratio=val_ratio,
                        images_path=images_path,
                        labels_path=labels_path)

    create_dataset_paths(dataset_path=dataset_path)

    copy_dataset_contents(dataset_path=dataset_path,
                        labels_path=labels_path,
                        splits=splits)

    create_yolo_yaml(dataset_path=dataset_path,
                     classes=classes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate YOLO datasets from images and YOLO annotations")
    parser.add_argument("--images-path", type=str, default="./images",
                        help="Path to the images to use in the dataset creation process (default: ./images)")
    parser.add_argument("--labels-path", type=str, default="./labels",
                        help="Path to the labels to use in the dataset creation process (default: ./labels)")
    parser.add_argument("--dataset-path", type=str, default="./dataset",
                        help="Path to the new dataset (default: ./dataset)")
    parser.add_argument("--class-file", type=str, default="./classes.txt",
                        help="Path to the .txt file containing the image names (default: ./images)")
    parser.add_argument("--train", type=float,
                        help="Train split ratio (default: 0.8)")
    parser.add_argument("--test", type=float,
                        help="Test split ratio (default: 0.1)")
    parser.add_argument("--val", type=float,
                        help="Validation split ratio (default: 0.1)")
    try:
        # Simplified argument parsing
        if "--" in sys.argv:
            argv = sys.argv[sys.argv.index("--") + 1:]
            logger.info(f"Command line arguments received: {argv}")
        else:
            argv = sys.argv[1:]  # Skip the script name
            
        args = parser.parse_args(argv)  # Parse the correct argument list
        logger.info(f"Parsed arguments: {args}")

        try:
            main(images=args.images_path,
                 labels=args.labels_path,
                 dataset=args.dataset_path,
                 class_file_path=args.class_file,
                 train_ratio=args.train,
                 test_ratio=args.test,
                 val_ratio=args.val)
        except Exception as e:
            logger.error(f"Error running main: {str(e)}")
            sys.exit(1)

    except Exception as e:
        logger.error(f"Error parsing arguments: {str(e)}")
        sys.exit(1)