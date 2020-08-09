<h2 align="center">supervisely-to-darknet</h2>
<p align="center"><b>Conversion from Supervisely JSON to Darknet Format via Python</b></p>

<br>

<h2>Table of Contents</h2>

<!-- TOC -->

- [Introduction](#introduction)
- [Usage](#usage)
- [Contributors](#contributors)
- [Maintainers](#maintainers)
- [References](#references)
- [License](#license)

<!-- /TOC -->


## Introduction

This repository shows a quick method to convert the JSON files exported by Supervisely annotation tool to the Darknet format in python language. Check it out!

## Usage

Clone the repository to your local path:

```bash
git clone https://github.com/JinhangZhu/supervisely-to-darknet.git
```

Copy the `convert.py` file into your local folder where the Supervisely `meta.json` is located. Open the terminal on Linux or command window in Windows.

help:

```shell
>python convert.py -h
usage: convert.py [-h] [-o ORIGIN] [-d DEST] [-m META] [-s] [-t TRAIN_SIZE]
                  [-v VAL_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  -o ORIGIN, --origin ORIGIN
                        The name of original data downloaded from Supervisely.
  -d DEST, --dest DEST  The name of the output dataset folder.
  -m META, --meta META  The name of the meta file of the data.
  -s, --shuffle         Whether to randomly split image set.
  -t TRAIN_SIZE, --train-size TRAIN_SIZE
                        Percentage of train set.
  -v VAL_SIZE, --val-size VAL_SIZE
                        Percentage of validation set.
```

For example, I have a folder called: "P30__P30_04" in the current path, I want to create a dataset folder called "P30", with randomly splitted subsets at the ratio: `train:validation:test`=0.9:0.1:0. I run:

```bash
python convert.py --origin P30__P30_04 --out P30 --shuffle --train-size 0.9 --val-size 0.1
```

Results:

```shell
└───P30                                                                   		
		├───images
		├───labels
				├───classes.names
				├───P30_train.txt
				├───P30_validation.txt
```

## Contributors

<table>
    <tbody>
        <tr>
            <td>
                <a href="https://github.com/jinhangzhu/supervisely-to-darknet/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=jinhangzhu/supervisely-to-darknet" />
</a>
        </tr>
    </tbody>
</table>

## Maintainers

[Jinhang Zhu](https://github.com/JinhangZhu)

## Thanks

- [ultralytics](https://github.com/ultralytics)/**[yolov3](https://github.com/ultralytics/yolov3)**

## License

- [MIT](https://opensource.org/licenses/MIT)
