#!/usr/bin/python3
"""Module base_Geometry
Creates a BaseGeometry class
"""


class BaseGeometry:
    """Class with public instance methods"""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
<<<<<<< HEAD
            raise ValueError("{} must be greater than 0".format(name))
=======
            raise ValueError("{} must be greater than 0".format(name))
>>>>>>> 53ceee224eea9badc22325c09efb0bb2e857c357
