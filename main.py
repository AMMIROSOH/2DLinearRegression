import numpy as np
import matplotlib.pyplot as plt
import math

class LinearRegression:
    def __init__(self, numbers, sliced = False):
        # Slicing the numbers Array to Xs & Ys
        if(not sliced):
            self.x_list = numbers[0: , 0]
            self.y_list = numbers[0: , 1]
            self.list_len = len(numbers)
        else:
            self.x_list = numbers[0]
            self.y_list = numbers[1]
            self.list_len = len(numbers[0])
        # Defineing Object Attributes
        self.x_average = None
        self.y_average = None
        self.correlation_coefficient = None
        self.slope = None
        self.y_intercept = None
        self.difference_square_x = 0.0
        self.difference_square_y = 0.0

        # Setting Attributes
        self.set_average()
        self.set_difference_square()
        self.set_correlation_coefficient()
        self.set_slope()
        self.set_y_intercept()
        # Loging the Attributes
        
        print(f"Correlation Coefficient: {self.correlation_coefficient} ***** Slope: {self.slope} ***** Y Intercept: {self.y_intercept}")

    def set_average(self):
        sx = 0.0
        sy = 0.0
        for i in range(0, self.list_len):
            sx += self.x_list[i]
            sy += self.y_list[i]
        self.x_average = sx/self.list_len
        self.y_average = sy/self.list_len
    
    def set_difference_square(self):
        # E(X - Xavg)**2 
        for i in range(0, self.list_len):
            self.difference_square_x += (self.x_list[i] - self.x_average)**2
            self.difference_square_y += (self.y_list[i] - self.y_average)**2

    def set_correlation_coefficient(self):
        # Correlation Coefficient Formula:
        # E( (X - Xavg)(Y - Yavg) )
        # ------------------------- #this is fraction line
        # Radical((E(X - Xavg)**2) * (E(Y - Yavg)**2))
        sum_numerator = 0.0
        sum_denominator_x = 0.0
        sum_denominator_y = 0.0
        for i in range(0, self.list_len):
            sum_numerator += (self.x_list[i] - self.x_average)*(self.y_list[i] - self.y_average)
        sum_denominator_x = self.difference_square_x
        sum_denominator_y = self.difference_square_y
        self.correlation_coefficient = sum_numerator/(math.sqrt(sum_denominator_x * sum_denominator_y))

    def set_slope(self):
        # Slope Formula:
        # Correlation Coefficient * ( standard_deviation_x / standard_deviation_y )
        standard_deviation_x = math.sqrt(self.difference_square_x / self.list_len)
        standard_deviation_y = math.sqrt(self.difference_square_y / self.list_len)
        self.slope = self.correlation_coefficient*(standard_deviation_y / standard_deviation_x)
        

    def set_y_intercept(self):
        # Y Intercept Formula:
        # Yavg - Slope * Xavg
        self.y_intercept = self.y_average - self.slope * self.x_average

    def draw(self):
        plt.plot(self.x_list, self.y_list, 'o')
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = self.y_intercept + self.slope * x_vals
        plt.plot(x_vals, y_vals, 'r')
        plt.show()


    def predictY(self, x):
        return (x * self.slope + self.y_intercept)

    def predictX(self, y):
        return ((y - self.y_intercept) / self.slope)
        

#ln = LinearRegression(np.array([[0, 5],[7, 8],[2, 9],[1, 4],[3, 9],[7, 8],[4, 6],[6, 0]]))
# print(ln.predictY(8))

