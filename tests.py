import unittest
from calculator import Calculator

class testCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.sum(6, 9), 14)

    def test_subtract(self):
        self.assertEqual(self.calculator.razn(16, 9), 7)

    def test_multiply(self):
        self.assertEqual(self.calculator.proiz(9, 9), 81)

    def test_devide(self):
        self.assertEqual(self.calculator.deli(24, 8), 3)

if __name__ == "__main__":
    unittest.main()