import unittest
from calculator import Calculator

class testCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.sum(6, 9), 1)
        self.assertEqual(self.calculator.sum(6, 91), 97)

    def test_subtract(self):
        self.assertEqual(self.calculator.razn(16, 9), 7)
        self.assertEqual(self.calculator.razn(90, 7), 83)

    def test_multiply(self):
        self.assertEqual(self.calculator.proiz(9, 9), 81)
        self.assertEqual(self.calculator.proiz(6, 8), 48)

    def test_devide(self):
        self.assertEqual(self.calculator.deli(24, 8), 3)
        self.assertEqual(self.calculator.deli(48, 4), 12)

if __name__ == "__main__":
    unittest.main()
