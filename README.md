# yolo-dataset-creator

## Requirements

The program requires an `images` directory containing image files and a `labels` directory containing YOLO formatted .txt files.

Supported image extensions:
- '.bmp'
- '.jpg'
- '.jpeg'
- '.png'
- '.tif'
- '.tiff' 
- '.dng'

## Output

The program splits the images into `train`, `test` and `val` sets and creates a dataset with said split.
- The split ratio is `80 / 10 / 10` for train, test and val respectively but the user can also provide their own default values.

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

