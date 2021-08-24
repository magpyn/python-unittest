import unittest


def area(width, height):
    """This function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError("The width and height must be of type int or float")

    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")

    return width * height


class TestArea(unittest.TestCase):

    def test_area1(self):
        self.assertEqual(area(4, 5), 20, "message")

    def test_area2(self):
        self.assertEqual(area(4, 5), 20, "message1")

    def test_area3(self):
        raise AssertionError("Error message")

    def test_area4(self):
        raise AssertionError("Error message")

if __name__ == "__main__":
    unittest.main(verbosity=2)