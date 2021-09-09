"""
Margaret Lehmann

HW 01 - This function takes three sides of a triangle and returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, and whether it is a right triangle.
"""
import unittest


def classify_triangle(a, b, c):
    triangleType = 'scalene'
    if a == b and b == c and a == c:
        triangleType = 'equilateral'
    elif a == b or b == c or a == c:
        triangleType = 'isosceles'

    isRightTriangle = False
    if (a * a + b * b) == c * c or \
        (a * a + c * c) == b * b or \
            (b * b + c * c) == a * a:
        isRightTriangle = True

    return (triangleType, isRightTriangle)


def triangleMain():
    type, right = classify_triangle(4, 4, 6)
    print("Triangle type = ", type, " Is Triangle right = ", right)

    type2, right2 = classify_triangle(10, 10, 10)
    print("Triangle type = ", type2, " Is Triangle right = ", right2)


class TestTriangles(unittest.TestCase):
    """ Unit test class to test classify_triangle """

    def testScalene(self):
        expectedRight = ('scalene', True)
        self.assertEqual(classify_triangle(3, 4, 5), expectedRight)

        expectedNotRight = ('scalene', False)
        self.assertEqual(classify_triangle(3, 4, 7), expectedNotRight)

    def testIsosceles(self):
        expectedNotRight = ('isosceles', False)
        self.assertEqual(classify_triangle(3, 3, 7), expectedNotRight)

    def testEquilateral(self):
        expectedNotRight = ('equilateral', False)
        self.assertEqual(classify_triangle(3, 3, 3), expectedNotRight)


if __name__ == '__main__':
    triangleMain()
    unittest.main(exit=False, verbosity=2)
