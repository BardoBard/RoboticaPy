import cv2
import numpy as np

from Information.ImageData import ImageData


class OpenCv:

    def detect_object(self, img):
        hierarchy_size = 0
        main_box = -1
        np.resize(img, img, {500, 500}, 0, 0, np.INTER_NEAREST)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thr = cv2.threshold(self.blur_difference(grey, 7, 7, 17, 13), 1, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contours)):
            contour_area = cv2.contourArea(contours[i])
            area_percentage = self.area_rotated_percentage(contours[i], contour_area)
            if contour_area > 1500 and hierarchy[i][3] == -1 and area_percentage > 30:
                a = 0
                for y in range(i + 1, len(hierarchy)):
                    contour_area_child = cv2.contourArea(contours[y])
                    area_percentage_child = self.area_rotated_percentage(contours[y], contour_area)
                    if hierarchy[y][3] == i and area_percentage_child > 30 and contour_area_child > 500:
                        a = a + 1
                        if a > hierarchy_size:
                            hierarchy_size = a
                            main_box = i

                            break
        if main_box == -1:
            return

        rotated_rect = cv2.minAreaRect(contours[main_box])
        rotated_area = rotated_rect.size.width * rotated_rect.size.height

        imagedata_ = ImageData(rotated_rect.center, rotated_rect.angle, cv2.contourArea(contours[main_box]),
                               cv2.contourArea(contours[main_box]) * (100.0 / rotated_area), rotated_area,
                               hierarchy_size, 250 - rotated_rect.center.x, rotated_rect.center.y - 250)
        imagedata_.command_line()

        return img

    def blur_difference(self, img, h1, s1, h2, s2):
        b1 = cv2.GaussianBlur(img, np.Size(h1, h1), s1)
        b2 = cv2.GaussianBlur(img, np.Size(h2, h2), s2)
        dif = b1 - b2
        return dif

    def area_rotated_percentage(self, contour, area):
        rotated_rect = cv2.minAreaRect(contour)
        rotated_area = rotated_rect.size.width * rotated_rect.size.height;
        return area * (100.0 / rotated_area)
