import unittest
from calculation import Calculation

class TestCalculation(unittest.TestCase):

    def test(self):
        calc = Calculation()
    # assertEqual(a, b) is one of the assertion methods provided by unittest. It checks that a and b are equal. If they are, the test passes. If they are not, the test fails
        self.assertEqual(calc.add(5), 5)
        self.assertEqual(calc.substract(1), 4)
        self.assertEqual(calc.multiply(4), 16)
        self.assertEqual(calc.divide(2), 8)
        self.assertEqual(calc.square(3), 9)
        self.assertEqual(calc.sqrt(4), 2)
        self.assertEqual(calc.pow(3,2), 9)

    # Here are some other assertion methods provided by unittest:
    
    # assertNotEqual(a, b): Fail if a and b are equal.
    # assertTrue(x): Fail if x is not True.
    # assertFalse(x): Fail if x is not False.
    # assertIn(a, b): Fail if a is not in b.
    # assertNotIn(a, b): Fail if a is in b.
    # assertIsNone(x): Fail if x is not None.
    # assertIsNotNone(x): Fail if x is None.


if __name__ == '__main__':
    unittest.main()

