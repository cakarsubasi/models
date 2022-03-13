import os

from omrdatasettools.Downloader import Downloader, OmrDataset

from image_color_inverter import ImageColorInverter

if __name__ == "__main__":
    muscima_pp_dataset_directory = os.path.join("data", "muscima_pp")
    muscima_image_directory = os.path.join(muscima_pp_dataset_directory, "v1.0", "data", "images")

    downloader = Downloader()
    downloader.download_and_extract_dataset(OmrDataset.MuscimaPlusPlus_V2, muscima_pp_dataset_directory)

    inverter = ImageColorInverter()
    # We would like to work with black-on-white images instead of white-on-black images
    inverter.invert_images(muscima_image_directory, "*.png")
