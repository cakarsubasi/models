import os
from itertools import groupby
from lxml import etree
from typing import List, Tuple

from lxml.etree import Element, SubElement
from mung.node import Node
from muscima.cropobject import CropObject


def create_annotations_in_pascal_voc_format_from_nodes(annotations_folder: str,
                                                       file_name: str,
                                                       nodes_appearing_in_image: List[Node],
                                                       image_width: int,
                                                       image_height: int,
                                                       image_depth: int):
    objects_appearing_in_image = []
    for detected_object in nodes_appearing_in_image:
        class_name = detected_object.class_name
        bounding_box = detected_object.bounding_box
        objects_appearing_in_image.append((file_name, class_name, bounding_box))

    create_annotations_in_pascal_voc_format(annotations_folder, file_name, objects_appearing_in_image,
                                            image_width, image_height, image_depth)


def create_annotations_in_pascal_voc_format(annotations_folder: str,
                                            file_name: str,
                                            objects_appearing_in_image: List[
                                                            Tuple[str, str, Tuple[int, int, int, int]]],
                                            image_width: int,
                                            image_height: int,
                                            image_depth: int):
    os.makedirs(annotations_folder, exist_ok=True)

    annotation = Element("annotation")
    folder = SubElement(annotation, "folder")
    folder.text = "muscima_pp_cropped_images"
    filename = SubElement(annotation, "filename")
    filename.text = file_name
    source = SubElement(annotation, "source")
    database = SubElement(source, "database")
    database.text = "MUSCIMA++"
    source_annotation = SubElement(source, "annotation")
    source_annotation.text = "MUSCIMA++ (v2.0)"
    image = SubElement(source, "image")
    image.text = "CVC-MUSCIMA"
    size = SubElement(annotation, "size")
    width = SubElement(size, "width")
    width.text = str(image_width)
    height = SubElement(size, "height")
    height.text = str(image_height)
    depth = SubElement(size, "depth")
    depth.text = str(image_depth)

    # Write results to file
    for detected_object in objects_appearing_in_image:
        file_name = detected_object[0]
        class_name = detected_object[1]
        translated_bounding_box = detected_object[2]
        ymin, xmin, ymax, xmax = translated_bounding_box

        object = SubElement(annotation, "object")
        name = SubElement(object, "name")
        name.text = class_name
        pose = SubElement(object, "pose")
        pose.text = "Unspecified"
        truncated = SubElement(object, "truncated")
        truncated.text = "0"
        difficult = SubElement(object, "difficult")
        difficult.text = "0"
        bndbox = SubElement(object, "bndbox")
        bb_xmin = SubElement(bndbox, "xmin")
        bb_xmin.text = str(xmin)
        bb_ymin = SubElement(bndbox, "ymin")
        bb_ymin.text = str(ymin)
        bb_xmax = SubElement(bndbox, "xmax")
        bb_xmax.text = str(xmax)
        bb_ymax = SubElement(bndbox, "ymax")
        bb_ymax.text = str(ymax)

    xml_file_path = os.path.join(annotations_folder, os.path.splitext(file_name)[0] + ".xml")
    pretty_xml_string = etree.tostring(annotation, pretty_print=True)

    with open(xml_file_path, "wb") as xml_file:
        xml_file.write(pretty_xml_string)
