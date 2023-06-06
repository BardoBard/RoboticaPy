import cv2
import numpy as np

from Information.ImageData import ImageData


class OpenCv:

    def detect_object(self, img):
        """
        :param img: gives the picture of video
        :return: returns imagedata
        """
        img_size = (1000, 1000)
        area_main = 1500
        area_child = 500

        hierarchy_size = 0
        main_box = -1  # if no contour fits requirements set -1 so no contour is gotten
        img = cv2.resize(img, img_size, 0, 0, cv2.INTER_NEAREST)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # use blur_difference to get the difference between 2 blurs

        ret, thr = cv2.threshold(self.blur_difference(grey, 7, 7, 17, 13), 1, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # loop for getting right contour
        for i in range(len(contours)):
            cnt = contours[i]

            # -1 means contour has no parent
            # 1500 is the area that needs to be checked
            if not self.loop_checks(cnt, i, hierarchy, -1, area_main):
                continue

            a = 0
            for y in range(i + 1, len(hierarchy[0])):
                cnr = contours[y]

                if not self.loop_checks(cnr, y, hierarchy, i, area_child):
                    continue

                if ++a < hierarchy_size:  # contour with the most amount of children
                    continue

                hierarchy_size = a
                main_box = i
                break

        if main_box == -1:
            return ImageData((0, 0), 0, 0, 0, 0, 0, 0, 0, img, False)

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
                               hierarchy_size, 250 - x, y - 250, crop_img, True)
        #imagedata_.command_line()

        return imagedata_

    def blur_difference(self, img, h1, s1, h2, s2):
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

    def area_rotated_percentage(self, contour, area):
        """
        :param contour: contour to calculate
        :param area: area of contour
        :return: how much does area of contour is equal to area of bounding box in percentage
        """
        rotated_rect = cv2.minAreaRect(contour)
        (width, height) = rotated_rect[1]
        rotated_area = width * height
        ar = area * (100.0 / rotated_area)
        return ar

    def loop_checks(self, cnt, i, hierarchy, hierarchy_ind, area):
        """
        :param cnt: contour that is being checked
        :param i: the index of contour
        :param hierarchy: 3 matrix of the hierarchy
        :param hierarchy_ind: index that the 4th element of the 3rd array of the hierarchy needs to be checked with
        :param area: the area that the contour will be checked with
        :return: false if it fails its checks, true if it doesn't
        """
        contour_area = cv2.contourArea(cnt)
        if contour_area < area:  # min area must be 500 pixels
            return False

        # in the 3rd array needs to check 3 element for parents
        if hierarchy[0][i][3] != hierarchy_ind:
            return False

        area_percentage = self.area_rotated_percentage(cnt, contour_area)

        if area_percentage < 30:  # percentage must be higher than 30
            return False
        return True
