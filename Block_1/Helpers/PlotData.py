class PlotData:
    x_coordinates = []
    y_coordinates = []
    x_data = 0

    @staticmethod
    def get_xy_coordinates(matrix):
        x_coordinates = []
        y_coordinates = []
        for bundle in matrix:
            x_coordinates.append(bundle[0])
            y_coordinates.append(bundle[1])
        return x_coordinates, y_coordinates

    def __init__(self, matrix, x_data=None):
        [x_coordinates, y_coordinates] = PlotData.get_xy_coordinates(matrix)
        self.set_coordinates(x_coordinates, y_coordinates)
        self.set_x_data_value(x_data)

    def set_coordinates(self, x_coordinates, y_coordinates):
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates

    def set_x_data_value(self, x_data):
        self.x_data = x_data

    def get_x_coordinates(self):
        return self.x_coordinates

    def get_y_coordinates(self):
        return self.y_coordinates

    def get_x_data_value(self):
        return self.x_data

    def elements_count(self):
        return len(self.y_coordinates)
