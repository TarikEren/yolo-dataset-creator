# yolo-dataset-creator

## Requirements

The program requires:
- a directory containing image files
    - Supported image extensions:
        - '.bmp'
        - '.jpg'
        - '.jpeg'
        - '.png'
        - '.tif'
        - '.tiff' 
        - '.dng'
- a directory containing YOLO formatted .txt files
- a .txt file containing class names
    - The class file should have one class name in each line. An example would be something like:
    ```
    class0
    class1
    class2
    ```

## Usage

Program arguments:
- --images-path: Path to the images to be used
    - Default: "./images"
- --labels-path: Path to the labels to be used
    - Default: "./labels",
- --dataset-path: Path to the new dataset
    - Default: "./dataset",
- --class-file: Path to the .txt file in which the classes are.
    - Default: "./classes.txt",
- --train: Train split ratio
- --test: Test split ratio
- --val: Validation split ratio
    
Example usage:
```bash
python ./main.py --train 0.8 --test 0.1 --val 0.1
```

- This usage would create a dataset named `new_dataset` and would read the classes from file `all_classes.txt`.

## Output

The program splits the images into `train`, `test` and `val` sets and creates a dataset with said split.

The created dataset directory tree is as follows:
```
.
└── dataset/
    ├── images/
    │   ├── train
    │   ├── test
    │   └── val
    └── labels/
        ├── train
        ├── test
        └── val
```

