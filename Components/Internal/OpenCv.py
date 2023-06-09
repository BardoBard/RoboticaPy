import cv2
from Information.ImageData import ImageData
from multiprocessing import Process, Queue

class OpenCv:
    """Contains our open CV box detection algorithms  
    """
    def __init__(self):
        self.__cap = cv2.VideoCapture(0) #Get a new video feed
        self.__image_size = 1000 #Images get resized to this size
    
    def get_image_date_from_feed(self) -> ImageData:
        """Tries to get an image from the video feed and detect if there's something there

        Raises:
            Exception: The image couldn't be captured

        Returns:
            ImageData: Class containing the best estimation of where the box is in the image
        """
        ret, img = self.__cap.read()
        
        if not ret:
            raise Exception("No image found")
        
        return self.__detect_object(img, self.__image_size)
    
    
    def __detect_object(self, img, size):
        """
        :param size: size of the image
        :param img: gives the picture of video
        :return: returns imagedata
        """
        img_size = (size, size)
        area_main = 3 * size
        area_child = size

        hierarchy_size = 0
        main_box = -1  # if no contour fits requirements set -1 so no contour is gotten
        img = cv2.resize(img, img_size, 0, 0, cv2.INTER_NEAREST)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # use blur_difference to get the difference between 2 blurs
        # first 7 is kernel size of first blur, second 7 is standard deviation of first blur image
        # 17 is kernel size of second blur, 13 is standard deviation of second blur image
        # 1 is the threshhold
        # 255 is the maxvalue
        ret, thr = cv2.threshold(self.__blur_difference(grey, 7, 7, 17, 13), 1, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # loop for getting right contour with i being index
        for i in range(len(contours)):
            contour = contours[i]

            # -1 means contour has no parent
            if not self.__loop_checks(contour, hierarchy[0][i][3] , -1, area_main):
                continue


            max_child = 0
            # y index of the child contour
            for y in range(i + 1, len(hierarchy[0])):
                contour_child = contours[y]

                if not self.__loop_checks(contour_child,hierarchy[0][y][3] , i, area_child):
                    continue
                
                max_child += 1
                # contour with the most amount of children will be taken with\
                if max_child < hierarchy_size:
                    continue

                hierarchy_size = max_child
                main_box = i
                break

        if main_box == -1:
            return ImageData((0, 0), 0, 0, 0, 0, 0, 0, 0, img, False, None) # empty imagedata

        rotated_rect = cv2.minAreaRect(contours[main_box])
        (x, y), (width, height), angle = rotated_rect
        rotated_area = width * height
        center = (int(x), int(y))
        size = (int(width), int(height))

        # calculate the rotation matrix
        matrix = cv2.getRotationMatrix2D(center, angle, 1)

        # rotate image
        img_rot = cv2.warpAffine(img, matrix, img_size)

        # crop image
        crop_img = cv2.getRectSubPix(img_rot, size, center)

        imagedata_ = ImageData(center, angle, cv2.contourArea(contours[main_box]),
                               cv2.contourArea(contours[main_box]) * (100.0 / rotated_area), rotated_area,
                               hierarchy_size, 250 - x, y - 250, crop_img, True, None)
        return imagedata_

    def __blur_difference(self, img, h1, s1, h2, s2):
        """
        :param img: img that gets blurred
        :param h1: kernel size of blur 1
        :param s1: standard deviation of blur 1
        :param h2: kernel size of blur 2
        :param s2: standard deviation of blur 2
        :return: an img of the differences between blur 1 and 2
        """
        b1 = cv2.GaussianBlur(img, (h1, h1), s1)
        b2 = cv2.GaussianBlur(img, (h2, h2), s2)
        dif = cv2.subtract(b1, b2)
        return dif

    def __area_rotated_percentage(self, contour, area):
        """
        :param contour: Contour to peform the calculation on
        :param area: Area of contour
        :return: Percentage of overlapping area between contour and and rotated area
        """
        rotated_rect = cv2.minAreaRect(contour)
        (width, height) = rotated_rect[1]
        rotated_area = width * height
        percentage = area * (100.0 / rotated_area)
        return percentage

    def __loop_checks(self, contour, hierarchy_parent, hierarchy_index_check, area):
        """
        :param contour: contour that is being checked
        :param hierarchy_parent: id of parent or -1 if no parent
        :param hierarchy_index_check: the one that the hierarchy parent needs to be checked against
        :param area: the area that the contour will be checked with
        :return: false if it fails its checks, true if it doesn't
        """
        contour_area = cv2.contourArea(contour)
        if contour_area < area:
            return False

        if hierarchy_parent != hierarchy_index_check:
            return False

        area_percentage = self.__area_rotated_percentage(contour, contour_area)

        if area_percentage < 30:
            return False
        return True
