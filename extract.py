"""Extract the *.tar files in a folder to unpressed folders under another path.
"""

import tarfile
import os
from tqdm import tqdm


def untar(dpath, xpath):
    for tar in tqdm(os.listdir(dpath), desc='Tar files'):
        filepath = os.path.join(dpath, tar)
        opened_tar = tarfile.open(filepath)
        opened_tar.extractall(xpath)
        opened_tar.close()


if __name__ == "__main__":
    # The path where *tar files are
    spath = "../datasets/supervisely/"
    # The path where the unpressed folders are
    dpath = "../datasets/supervisely_raw"

    untar(dpath, spath)
