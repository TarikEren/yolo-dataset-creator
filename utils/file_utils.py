from pathlib import Path

from .logger_utils import logger

def create_yolo_yaml(dataset_path: Path, classes: list[str]) -> None:
    """
    Creates the data.yaml file for YOLO to use

    Args:
        dataset_path (Path): Path to the dataset root
        classes (list[str]): List of class names in order.

    Returns:
        None
    """

    class_dict = {}
    for i in range(len(classes)):
        class_dict[f"{i}"] = classes[i]

    yaml_path = Path("data.yaml")

    if Path.exists(yaml_path):
        logger.warning(f"{yaml_path} already exists. Skipping creation")

    else:
        try:
            with open(yaml_path, "w") as file:
                file.write(f"""path: {dataset_path}     # The dataset root

train: {"images/train"}     # Path to train
test: {"images/test"}       # Path to test
val: {"images/val"}         # Path to val

names:  # Class names
""")
                for item in class_dict:
                    file.write(f"    {item}: {class_dict[item]}\n")
        except Exception as e:
            logger.error(f"Error creating data.yaml: {str(e)}")
            raise Exception(f"Error creating data.yaml: {str(e)}")
        
    logger.info("Successfully created data.yaml")

def read_classes(class_file: str) -> list[str]:
    """
    Reads the provided text file classes text file.

    Args:
        class_file (str): Path to the class file

    Returns:
        list(str): List of classes
    """

    with open(class_file, "r") as file:
        classes = [line.rstrip() for line in file]

    logger.info(f"Read classes: {classes}")
    return classes