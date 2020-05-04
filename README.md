<h2 align="center">supervisely-to-darknet</h2>
<p align="center"><b>Conversion from Supervisely JSON to Darknet Format via Python</b></p>

<br>

<h2>Table of Contents</h2>

<!-- TOC -->

- [Introduction](#introduction)
- [Usage](#usage)
- [Contributors](#contributors)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [License](#license)

<!-- /TOC -->


## Introduction

This repository shows a quick method to convert the JSON files exported by Supervisely annotation tool to the Darknet format in python language. Check it out!

## Usage

Clone the repository to your local path:

```bash
git clone https://github.com/JinhangZhu/supervisely-to-darknet.git
```

Open the terminal on Linux or command window in Windows and run:

```bash
python convert.py --origin ...
```

help:

- `--origin`: The name of original data downloaded from Supervisely.
- `--out`: The name of the output dataset folder.
- `--meta`: The name of the meta file of the data.
- `--shuffle`: Whether to randomly split image set.
- `--train-size`: Percentage of train set.
- `--val-size`: Percentage of validation set.

For example, I have a folder called: "P30__P30_04" in the current path, I want to create a dataset folder called "P30", with randomly splitted subsets at the ratio: `train:validation:test`=0.9:0.1:0. I run:

```bash
python convert.py --origin 'P30__P30_04' --out 'new' --meta 'meta.json' --shuffle True --train-size 0.9 --val-size 0.1
```

Results:

![](https://i.loli.net/2020/05/03/DRSMpJBNyv73o9C.png)

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
