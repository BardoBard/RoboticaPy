class ImageData:
    center = (0, 0)  # maybe install library or make class with center
    angle = 0.0  # float
    contour_area = 0.0
    contour_percentage = 0.0  # double
    rotated_area = 0
    kids = 0
    movex = 0
    movey = 0  # int
    image = None
    found = False
    matrix_code = None

    # default constructor
    def __int__(self):
        return

    def __init__(self, center, angle, contour_area, contour_percentage, rotated_area, kids, movex, movey,image, found, matrix_code):
        self.center = center
        self.angle = angle
        self.contour_area = contour_area
        self.contour_percentage = contour_percentage
        self.rotated_area = rotated_area
        self.kids = kids
        self.movex = movex
        self.movey = movey
        self.image = image
        self.found = found
        self.matrix_code = matrix_code

    def print_to_command_line(self):
        print("===========================")
        print("center: %s"              % (self.center))
        print("angle: %s"               % (self.angle))
        print("countour area: "         % (self.contour_area))
        print("countour percentage: %s" % (self.contour_percentage))
        print("rotated area: %s"        % (self.rotated_area))
        print("children: %s"            % (self.kids))
        print("move X: %s"              % (self.movex))
        print("move Y: %s"              % (self.movey))
        print("matrix_code: %s"         % (self.matrix_code))
        print("===========================")
