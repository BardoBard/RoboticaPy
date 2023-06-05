import cv2
import unittest
import xml.etree.cElementTree as ET
import os
import glob

from Components.Internal.OpenCv import OpenCv

image_dir = os.path.join(os.getcwd() + "\\Images\\")
resize_size = 500  # TODO: perhaps integrate this with opencv
offset = 40


# TODO: put xml parsing here and return image_information (or reference)
# def parse_xml(filename, center, xmin, ymin, xmax, ymax):

class MyTestCase(unittest.TestCase):
    def test_something(self):
        xml_files = glob.glob(image_dir + "*.xml")
        cv = OpenCv()

        for file in xml_files:
            file_name = os.path.splitext(os.path.basename(file))[0]
            # load the xml file
            doc = ET.parse(image_dir + file_name + ".xml")

            # read the image
            image = cv2.imread(image_dir + file_name + ".jpg", cv2.IMREAD_GRAYSCALE)

            if image is None:
                self.fail("image not found")

            # initialization
            root = doc.getroot()
            object_elem = root.find("object")

            # get the rectangle coordinates
            bndbox = object_elem.find("bndbox")
            xmin = int(bndbox.find("xmin").text)
            ymin = int(bndbox.find("ymin").text)
            xmax = int(bndbox.find("xmax").text)
            ymax = int(bndbox.find("ymax").text)

            # calculate the center of the rectangle
            center = ((xmin + xmax) / 2.0, (ymin + ymax) / 2.0)

            height, width = image.shape

            # normalize points to set size
            normalized_center = (
                center[0] / width * resize_size, center[1] / height * resize_size)

            # detect object
            data = cv.detect_object(image)  # TODO: change this to include reference to image_data

            if data is None:
                self.fail("there is no object in the image, but there should be")

            self.assertEqual(normalized_center[1] - offset <= data.center[1] <= normalized_center[1] + offset)

            # TODO: this can be done more efficiently, but it's fine for now
            # normalize area of rectangle
            normalized_area = (xmax / width * resize_size - xmin / width * resize_size) * (
                    ymax / height * resize_size - ymin / height * resize_size)

            # result area of rectangle
            result_area = data.area

            # check if area is within acceptable range
            self.assertEqual(0.8 < result_area / normalized_area < 1.2)

    if __name__ == '__main__':
        unittest.main()
