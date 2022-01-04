from Block_1.Helpers.PlotData import PlotData

class FiveStepsCoordinate:
    plot_data = None

    x_plus_2h = None
    x_plus_h = None
    x = None
    x_minus_h = None
    x_minus_2h = None

    def __init__(self, plot_data: PlotData):
        self.plot_data = plot_data

        y_coordinates = plot_data.get_y_coordinates()
        self.broke_coordinates_into_steps(y_coordinates)

    def broke_coordinates_into_steps(self, y_coordinates):
        #  [f(x-2h), f(x-h), f(x), f(x+h), f(x+2h)] => [0, 1 , 2, -2, -1]
        self.x_plus_2h = y_coordinates[0]
        self.x_plus_h = y_coordinates[1]
        self.x = y_coordinates[2]
        self.x_minus_h = y_coordinates[-2]
        self.x_minus_2h = y_coordinates[-1]

    def get_y_coordinates(self):
        if self.plot_data is None:
            raise ValueError("PlotData has not been initialized")

        return self.plot_data.get_y_coordinates()

class FiveStepsCoordinateForward:
    plot_data = None

    x = None
    x_plus_h = None
    x_plus_2h = None
    x_plus_3h = None
    x_plus_4h = None

    def __init__(self, plot_data: PlotData):
        self.plot_data = plot_data

        y_coordinates = plot_data.get_y_coordinates()
        self.broke_coordinates_into_steps(y_coordinates)

    def broke_coordinates_into_steps(self, y_coordinates):
        #  [f(x-2h), f(x-h), f(x), f(x+h), f(x+2h)] => [0, 1 , 2, -2, -1]
        self.x = y_coordinates[0]
        self.x_plus_h = y_coordinates[1]
        self.x_plus_2h = y_coordinates[2]
        self.x_plus_3h = y_coordinates[3]
        self.x_plus_4h = y_coordinates[4]

    def get_y_coordinates(self):
        if self.plot_data is None:
            raise ValueError("PlotData has not been initialized")

        return self.plot_data.get_y_coordinates()


class FiveStepsCoordinateBackward:
    plot_data = None
    x = None
    x_minus_h = None
    x_minus_2h = None
    x_minus_3h = None
    x_minus_4h = None

    def __init__(self, plot_data: PlotData):
        self.plot_data = plot_data

        y_coordinates = plot_data.get_y_coordinates()
        self.broke_coordinates_into_steps(y_coordinates)

    def broke_coordinates_into_steps(self, y_coordinates):
        #  [f(x-2h), f(x-h), f(x), f(x+h), f(x+2h)] => [0, 1 , 2, -2, -1]
        self.x = y_coordinates[0]
        self.x_minus_h = y_coordinates[1]
        self.x_minus_2h = y_coordinates[2]
        self.x_minus_3h = y_coordinates[3]
        self.x_minus_4h = y_coordinates[4]

    def get_y_coordinates(self):
        if self.plot_data is None:
            raise ValueError("PlotData has not been initialized")

        return self.plot_data.get_y_coordinates()
