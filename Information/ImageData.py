class ImageData:
    center = (0, 0)  # maybe install library or make class with center
    angle = 0.0  # float
    contour_area, contour_percentage = 0.0  # double
    rotated_area, kids, movex, movey = 0  # int

    # default constructor
    def __int__(self):
        return

    def __init__(self, center, angle, contour_area, contour_percentage, rotated_area, kids, movex, movey):
        self.center = center
        self.angle = angle
        self.contour_area = contour_area
        self.contour_percentage = contour_percentage
        self.rotated_area = rotated_area
        self.kids = kids
        self.movex = movex
        self.movey = movey

    def command_line(self):
        return  # void
