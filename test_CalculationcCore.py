import unittest
from CalculationCore import evaluate_expression
import math

class TestCalculatorCore(unittest.TestCase):

    def test_basic_arithmetic(self):
        self.assertEqual(evaluate_expression("2+3"), "5")
        self.assertEqual(evaluate_expression("10-4"), "6")
        self.assertEqual(evaluate_expression("5*6"), "30")
        self.assertEqual(evaluate_expression("8/2"), "4.0")

    def test_scientific_functions(self):
        self.assertAlmostEqual(float(evaluate_expression("sin(30)")), 0.5, places=5)
        self.assertAlmostEqual(float(evaluate_expression("cos(60)")), 0.5, places=5)
        self.assertAlmostEqual(float(evaluate_expression("tan(45)")), 1.0, places=5)
        self.assertEqual(evaluate_expression("log(100)"), "2.0")
        self.assertEqual(evaluate_expression("ln(1)"), "0.0")
        self.assertEqual(evaluate_expression("√(9)"), "3.0")
        self.assertEqual(evaluate_expression("2^3"), "8")

    def test_constants(self):
        self.assertEqual(evaluate_expression("π"), str(math.pi))
        self.assertEqual(evaluate_expression("e"), str(math.e))

    def test_factorials(self):
        self.assertEqual(evaluate_expression("5!"), "120")
        self.assertEqual(evaluate_expression("(3+2)!"), "120")

    def test_invalid_expression(self):
        self.assertEqual(evaluate_expression("5*/2"), "Error")
        self.assertEqual(evaluate_expression("√(abc)"), "Error")

if __name__ == '__main__':
    unittest.main()
