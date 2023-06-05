import cv2
import numpy as np

from Information.ImageData import ImageData


class OpenCv:

    def detect_object(self, img):
        hierarchy_size = 0
        main_box = -1
        img = cv2.resize(img, (500, 500), 0, 0, cv2.INTER_NEAREST)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thr = cv2.threshold(self.blur_difference(grey, 7, 7, 17, 13), 1, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        
        for i in range(len(contours)):
            cnt = contours[i]
            contour_area = cv2.contourArea(cnt)
            if contour_area < 1500: 
                continue
            
            area_percentage = self.area_rotated_percentage(cnt, contour_area)
            
            if hierarchy[0][i][3] != -1:
                continue
            
            if area_percentage < 30:
                continue
            
            a = 0
            for y in range(i + 1, len(hierarchy[0])):
                cnr = contours[y]
                contour_area_child = cv2.contourArea(cnr)
                
                if contour_area_child < 50:
                    continue
                
                area_percentage_child = self.area_rotated_percentage(cnr, contour_area)
                
                if hierarchy[0][y][3] != i:
                    continue
                
                if area_percentage_child < 30:
                    continue
                
                a = a + 1
                
                if a < hierarchy_size:
                    continue
                 
                hierarchy_size = a
                main_box = i
                break

        if main_box == -1:
            return img

        rotated_rect = cv2.minAreaRect(contours[main_box])
        (x, y), (width, height), angle = rotated_rect
        rotated_area = width * height
        center = (int(x), int(y))
        boxpoints = cv2.boxPoints(rotated_rect)  # todo remove for pi
        box = np.int0(boxpoints)  # todo remove for pi

        for i in range(4):
            cv2.line(img, box[i], box[(i + 1) % 4], (255, 20, 200))  # todo remove for pi

        imagedata_ = ImageData(center, angle, cv2.contourArea(contours[main_box]),
                               cv2.contourArea(contours[main_box]) * (100.0 / rotated_area), rotated_area,
                               hierarchy_size, 250 - x, y - 250)
        imagedata_.command_line()

        h = int(height)
        w = int(width)
        y = int(y)
        x = int(x)

        height, width = img.shape[0], img.shape[1]

        # calculate the rotation matrix
        M = cv2.getRotationMatrix2D(center, angle, 1)
        img_rot = cv2.warpAffine(img, M, (height, width))
        crop_img = cv2.getRectSubPix(img_rot, (w, h), center)

        return crop_img

    def blur_difference(self, img, h1, s1, h2, s2):
        b1 = cv2.GaussianBlur(img, (h1, h1), s1)
        b2 = cv2.GaussianBlur(img, (h2, h2), s2)
        dif = cv2.subtract(b1, b2)
        return dif

    def area_rotated_percentage(self, contour, area):
        rotated_rect = cv2.minAreaRect(contour)
        (x, y), (width, height), angle = rotated_rect
        rotated_area = width * height
        ar = area * (100.0 / rotated_area)
        return ar
