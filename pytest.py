import unittest
import circle
import triangle
import rectangle
import square

class circleTestCase(unittest.TestCase):
    def test_negative_values_and_zero(self):
        self.assertEqual(circle.area(-10), "Error: Length must be an integer >0")
        self.assertEqual(circle.circumference(-10), "Error: Length must be an integer >0")
        self.assertEqual(circle.area(0), "Length can't be zero")
        self.assertEqual(circle.circumference(0), "Length can't be zero")

    def test_string(self):
        self.assertEqual(circle.area("abc"), "Error: Length must be an integer >0")
        self.assertEqual(circle.circumference("abc"), "Error: Length must be an integer >0")

    def test_float(self):
        self.assertEqual(circle.area(0.1), "Error: Length must be an integer >0")
        self.assertEqual(circle.circumference(0.1), "Error: Length must be an integer >0")

class triangleTestCase(unittest.TestCase):
    def test_negative_values_and_zero(self):
        self.assertEqual(triangle.area(-10, 5), "Error: Length must be an integer >0")
        self.assertEqual(triangle.perimeter(-10, 5, 1), "Error: Length must be an integer >0")
        self.assertEqual(triangle.area(10, 0), "Length can't be zero")
        self.assertEqual(triangle.perimeter(10, 5, 0), "Length can't be zero")

    def test_string(self):
        self.assertEqual(triangle.area(10, "abcd"), "Error: Length must be an integer >0")
        self.assertEqual(triangle.perimeter(10, 5, "abcd"), "Error: Length must be an integer >0")

    def test_float(self):
        self.assertEqual(triangle.area(10, 0.5), "Error: Length must be an integer >0")
        self.assertEqual(triangle.perimeter(10, 5, 0.5), "Error: Length must be an integer >0")

class squareTestCase(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(square.area(-10), "Error: Length must be an integer >0")
        self.assertEqual(square.perimeter(-10), "Error: Length must be an integer >0")

    def test_zero(self):
        self.assertEqual(square.area(0), "Length can't be zero")
        self.assertEqual(square.perimeter(0), "Length can't be zero")

    def test_string(self):
        self.assertEqual(square.area("abc"), "Error: Length must be an integer >0")
        self.assertEqual(square.perimeter("abc"), "Error: Length must be an integer >0")

    def test_float(self):
        self.assertEqual(square.area(0.5), "Error: Length must be an integer >0")
        self.assertEqual(square.perimeter(0.5), "Error: Length must be an integer >0")

class rectangleTestCase(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(rectangle.area(-10, 5), "Error: Length must be an integer >0")
        self.assertEqual(rectangle.perimeter(-10, 5), "Error: Length must be an integer >0")

    def test_zero(self):
        self.assertEqual(rectangle.area(10, 0), "Length can't be zero")
        self.assertEqual(rectangle.perimeter(10, 0), "Length can't be zero")

    def test_string(self):
        self.assertEqual(rectangle.area(10, "abc"), "Error: Length must be an integer >0")
        self.assertEqual(rectangle.perimeter(10, "abc"), "Error: Length must be an integer >0")

    def test_float(self):
        self.assertEqual(rectangle.area(10, 0.5), "Error: Length must be an integer >0")
        self.assertEqual(rectangle.perimeter(10, 0.5), "Error: Length must be an integer >0")

if __name__ == '__main__':
    unittest.main()
