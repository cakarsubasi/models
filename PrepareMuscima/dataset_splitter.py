import argparse
import os
import random
import shutil
from typing import List
import re

import numpy
import numpy as np

from sklearn.model_selection import train_test_split


class DatasetSplitter:
    """ Class that can be used to create a reproducible random-split of a dataset into train/validation/test sets """

    def __init__(self,
                 source_directory: str,
                 destination_directory: str,
                 independent_set: str):
        """
        :param source_directory: The root directory, where all images currently reside.
        :param destination_directory: The root directory, into which the data will be placed.
            Inside of this directory, the following structure will be created:

         destination_directory
         |- training
         |
         |- validation
         |
         |- test

        """
        self.source_directory = source_directory
        self.destination_directory = os.path.abspath(destination_directory)
        self.independent_set = independent_set

    def get_independent_training_validation_and_test_sample_indices(
            self, validation_percentage=0.16, seed: int = 0):
        """
        Returns a reproducible set of sample indices from the entire dataset population following independent writer splitting
        :param validation_percentage: the percentage of the entire population size that should be used for validation
        :return: A triple of three list, containing indices of the training, validation and test sets
        """
        random.seed(seed)
        test_set_names = np.genfromtxt(self.independent_set, dtype=str, delimiter="\n")
        image_name_regex = re.compile(r".*W-(?P<writer>\d+)_N-(?P<page>\d+).*")
        test_set_writer_page = [image_name_regex.match(x) for x in test_set_names]
        test_set_writer_page = [[int(x.group("writer")), int(x.group("page"))]
                                for x in test_set_writer_page]
        names = os.listdir(self.source_directory)
        test_set_indices = []
        training_set_indices = []
        for i, name in enumerate(names):
            name_result = image_name_regex.match(name)
            writer = int(name_result.group("writer"))
            page = int(name_result.group("page"))
            if [writer, page] in test_set_writer_page:
                test_set_indices.append(i)
            else:
                training_set_indices.append(i)
        training_set_indices, validation_set_indices = \
            train_test_split(training_set_indices, test_size=validation_percentage)
        return training_set_indices, validation_set_indices, test_set_indices

    def delete_split_directories(self):
        print("Deleting split directories... ")
        shutil.rmtree(os.path.join(self.destination_directory, "train"), True)
        shutil.rmtree(os.path.join(self.destination_directory, "validation"), True)
        shutil.rmtree(os.path.join(self.destination_directory, "test"), True)

    def split_images_into_training_validation_and_test_set(self):
        print("Splitting data into training, validation and test sets...")

        training_sample_indices, validation_sample_indices, test_sample_indices = \
            self.get_independent_training_validation_and_test_sample_indices()

        self.copy_files(self.source_directory, training_sample_indices, "training")
        self.copy_files(self.source_directory, validation_sample_indices, "validation")
        self.copy_files(self.source_directory, test_sample_indices, "test")

    def copy_files(self, path_to_images_of_class, sample_indices, name_of_split):
        files = numpy.array(os.listdir(path_to_images_of_class))[sample_indices]
        destination_path = os.path.join(self.destination_directory, name_of_split)
        os.makedirs(destination_path, exist_ok=True)
        print("Copying {0} {1} files...".format(len(files), name_of_split))

        with open(os.path.join(self.destination_directory, name_of_split + ".txt"), "w") as image_set_dump:
            for image in files:
                image_set_dump.write(os.path.splitext(image)[0] + "\n")
                shutil.copy(os.path.join(path_to_images_of_class, image), destination_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_directory",
        type=str,
        default="data/muscima_pp/v2.0/data/images",
        help="The directory, where the images should be copied from")
    parser.add_argument(
        "--destination_directory",
        type=str,
        default="data/training_validation_test",
        help="The directory, where the images should be split into the three directories 'train', 'test' and "
             "'validation'")
    parser.add_argument(
        "--independent_set",
        type=str,
        default="data/muscima_pp/v2.0/specifications/testset-independent.txt",
        help="text file with independent writer set")

    flags, unparsed = parser.parse_known_args()

    datasest = DatasetSplitter(flags.source_directory, flags.destination_directory,
                               flags.independent_set)
    datasest.delete_split_directories()
    datasest.split_images_into_training_validation_and_test_set()
