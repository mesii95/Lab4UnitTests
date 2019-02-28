import unittest

from Rational import Rational

# Author: Archie Zwerlein


class MyTestCase(unittest.TestCase):
    frac = Rational(0, 1)

    # Test with a positive number
    def test_float_positive(self):
        frac = Rational(10, 5)
        self.assertEqual(2.0, frac.__float__())

    # Test with a negative number
    def test_float_negative(self):
        frac = Rational(-5, 1)
        self.assertEqual(-5.0, frac.__float__())

    # Test with n = 0
    def test_float_zero(self):
        frac = Rational(0, 1)
        self.assertEqual(0.0, frac.__float__())

    # Test with 0<n<d
    def test_float_positive_frac_less(self):
        frac = Rational(4, 5)
        self.assertEqual(0.8, frac.__float__())

    # Test with d<n<0
    def test_float_negative_frac_less(self):
        frac = Rational(-4, 5)
        self.assertEqual(-0.8, frac.__float__())

    # Test with 0<d<n
    def test_float_positive_frac_greater(self):
        frac = Rational(9, 5)
        self.assertEqual(1.8, frac.__float__())

    # Test with n<d<0
    def test_float_negative_frac_greater(self):
        frac = Rational(-9, 5)
        self.assertEqual(-1.8, frac.__float__()) 
