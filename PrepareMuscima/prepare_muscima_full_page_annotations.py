import os
import shutil
from glob import glob

from PIL import Image
from tqdm import tqdm
from mung.io import read_nodes_from_file


from muscima_annotation_generator import create_annotations_in_pascal_voc_format_from_nodes


def prepare_annotations(muscima_pp_dataset_directory: str,
                        exported_annotations_file_path: str,
                        annotations_path: str):
    muscima_image_directory = os.path.join(muscima_pp_dataset_directory, "v2.0", "data", "images", "*.png")
    image_paths = glob(muscima_image_directory)

    xml_annotations_directory = os.path.join(muscima_pp_dataset_directory, "v2.0", "data", "annotations")
    all_xml_files = [y for x in os.walk(xml_annotations_directory) for y in glob(os.path.join(x[0], '*.xml'))]

    if os.path.exists(exported_annotations_file_path):
        os.remove(exported_annotations_file_path)

    shutil.rmtree(annotations_path, ignore_errors=True)

    for xml_file in tqdm(all_xml_files, desc='Parsing annotation files'):
        nodes = read_nodes_from_file(xml_file)
        doc = nodes[0].document

        image_path = None
        for path in image_paths:
            if doc in path:
                image_path = path
                break

        image = Image.open(image_path, "r")  # type: Image.Image
        image_width = image.width
        image_height = image.height
        create_annotations_in_pascal_voc_format_from_nodes(annotations_path,
                                                           os.path.basename(image_path),
                                                           nodes,
                                                           image_width,
                                                           image_height,
                                                           3)


if __name__ == "__main__":
    muscima_pp_dataset_directory = os.path.join("data", "muscima_pp")
    prepare_annotations(muscima_pp_dataset_directory, "data/Full_Page_Annotations.csv", "data/Full_Page_Annotations")
