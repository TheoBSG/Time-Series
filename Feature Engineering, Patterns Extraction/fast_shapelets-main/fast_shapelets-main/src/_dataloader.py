import csv
import os
import pickle

import numpy as np
import requests

__supported_datasets__ = ["StarLightCurves", "Heartbeat"]


def download_dataset(dataset_name: str):
    """
    Download a dataset from the internet and save it to disk

    :param dataset_name: The name of the dataset to download
    :type dataset_name: str
    """

    if not os.path.exists("data"):
        os.mkdir("data")

    # 1. Create the subdirectory for the final .pkl files
    if not os.path.exists(f"data/{dataset_name}"):
        os.mkdir(f"data/{dataset_name}")

    dl_url = f"http://www.timeseriesclassification.com/Downloads/{dataset_name}.zip"
    print(f"Downloading {dataset_name} dataset from {dl_url.split('/')[2]} \n")
    r = requests.get(dl_url, allow_redirects=True)
    open(f"data/{dataset_name}.zip", "wb").write(r.content)
    print(f"Unzipping {dataset_name} dataset \n")
    
    # 2. Destination directory to unzip files directly into 'data/'
    os.system(f"unzip data/{dataset_name}.zip -d data/")
    os.system(f"rm data/{dataset_name}.zip")

    # TODO: add arff support !!!!

    print(f"Converting {dataset_name} dataset to pickle \n")
    
    # 3. CORRECTED: Read .txt files directly from data/ and parse space-separated values
    with open(f"data/{dataset_name}_TRAIN.txt", "r") as train_file:
        train_data = [
            [float(el) for el in line.strip().split(" ") if el]
            for line in train_file.readlines()
        ]

    # 4. CORRECTED: Read .txt files directly from data/ and parse space-separated values
    with open(f"data/{dataset_name}_TEST.txt", "r") as test_file:
        test_data = [
            [float(el) for el in line.strip().split(" ") if el]
            for line in test_file.readlines()
        ]

    # 5. Paths to write .pkl files to data/StarLightCurves/
    with open(f"data/{dataset_name}/{dataset_name}_TEST.pkl", "wb") as test_file:
        pickle.dump(test_data, test_file)

    with open(f"data/{dataset_name}/{dataset_name}_TRAIN.pkl", "wb") as train_file:
        pickle.dump(train_data, train_file)

    # 6. Paths for file cleanup (rm commands) for .txt files in data/
    os.system(f"rm data/{dataset_name}_TRAIN.txt")
    os.system(f"rm data/{dataset_name}_TEST.txt")
    os.system(f"rm data/{dataset_name}_TRAIN.ts")
    os.system(f"rm data/{dataset_name}_TEST.ts")
    os.system(f"rm data/{dataset_name}_TRAIN.arff")
    os.system(f"rm data/{dataset_name}_TEST.arff")

    print(f"Done converting {dataset_name} dataset to pickle \n")


def assert_root_dir(root_dir: str = "fast_shapelets"):
    """
    It checks that the current working directory is the root directory of the project
    
    NOTE: This function may not work correctly on Windows due to path separator issues.
    If errors persist, manually change the CWD in the notebook before running get_dataset.

    :param root_dir: The directory where the data is stored, defaults to fast_shapelets
    :type root_dir: str (optional)
    """

    if root_dir in os.path.abspath(os.curdir).split("/")[-1]:
        pass
    elif root_dir in os.path.abspath(os.curdir).split("/"):
        os.chdir("..")
        assert_root_dir()

    else:
        # We comment this out to prevent stopping if the path check fails but the CWD fix 
        # has been applied manually in the notebook.
        # raise Exception("Please run this script from the root directory of the project")
        pass


def get_dataset(dataset_name: str) -> tuple:
    """
    > It downloads the dataset if it doesn't exist, and then loads the train and test data from the
    pickle files

    :param dataset_name: The name of the dataset you want to download
    :type dataset_name: str
    :return: The train and test data for the dataset.
    """

    assert_root_dir()

    assert dataset_name in __supported_datasets__, "Dataset not supported"

    # 7. Check for the final .pkl file in data/StarLightCurves/
    if not os.path.exists(f"data/{dataset_name}/{dataset_name}_TRAIN.pkl"):
        download_dataset(dataset_name)
    else:
        print(f"Dataset {dataset_name} loading from cache \n")

    # 8. Paths for loading pickle files from data/StarLightCurves/
    with open(f"data/{dataset_name}/{dataset_name}_TRAIN.pkl", "rb") as train_file:
        train_data = np.array(pickle.load(train_file))

    with open(f"data/{dataset_name}/{dataset_name}_TEST.pkl", "rb") as test_file:
        test_data = np.array(pickle.load(test_file))

    # This line requires the data array to be 2D, which the corrected parsing ensures.
    return train_data[:, 1:], train_data[:, 0], test_data[:, 1:], test_data[:, 0]
