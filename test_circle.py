import unittest   
from example1 import Circle    
class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # the value of c1.radius is equal to 2.5 or not.
        c1=Circle(2.5)
        self.assertEqual(c1.radius,2.5)

    def test_creating_circle_with_negative_radius(self):
        # Define a circle 'c' with radius -2.5, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        with self.assertRaises(ValueError):
            c1=Circle(-2.5)
            c1.radius

    def test_creating_circle_with_greaterthan_radius(self):
        # Define a circle 'c' with radius 1000.1, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive". 
        with self.assertRaises(ValueError):
            c1=Circle(1000.1)
            c1.radius       
        
    def test_creating_circle_with_nonnumeric_radius(self):
        # Define a circle 'c' with radius 'hello' and check 
        # if it raises a TypeError with the message
        # "radius must be a number". 
        with self.assertRaises(TypeError):
            c1=Circle("Hello")
            c1.radius          
        
     