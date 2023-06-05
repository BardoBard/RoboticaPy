class ImageData:
    center = (0, 0)  # maybe install library or make class with center
    angle = 0.0  # float
    contour_area = 0.0
    contour_percentage = 0.0  # double
    rotated_area = 0
    kids = 0
    movex = 0
    movey = 0  # int

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
        print(self.center)
        print(self.angle)
        print(self.contour_area)
        print(self.contour_percentage)
        print(self.rotated_area)
        print(self.kids)
        print(self.movex)
        print(self.movey)



        return  # void
