import unittest
from Modules.Rational import Rational
# Written by: Alexandru Bozdog

class DivTests(unittest.TestCase):

    fac1 = Rational()
    frac2 = Rational()
    quotient = Rational()

    def equaldivision(self):
        frac1 = Rational(5, 5)
        frac2 = Rational(6, 6)

        quotient = frac1.__sub__(frac2)

        self.assertEqual(0, quotient.n)
        self.assertEqual(1, quotient.d)

    def testsubtractingnegative(self):
        frac1 = Rational(2, 5)
        frac2 = Rational(-6, 10)

        quotient = frac1.__sub__(frac2)

        self.assertEqual(0, quotient.n)
        self.assertEqual(1, quotient.d)

    def testtopnumberchangeonly(self):
        frac1 = Rational(3, 5)
        frac2 = Rational(2, 5)

        quotient = frac1.__sub__(frac2)

        self.assertEqual(0, quotient.n)
        self.assertEqual(1, quotient.d)

    def bottomnumberchangeonly(self):
        frac1 = Rational(1, 10)
        frac2 = Rational(1, 5)

        quotient = frac2.__sub__(frac1)

        self.assertEqual(1, quotient.n)
        self.assertEqual(10, quotient.d)

    def subtractingzerovalue(self):
        frac1 = Rational(5, 2)
        frac2 = Rational(0,100)

        quotient = frac1.__sub__(frac2)

        self.assertEqual (5, quotient.n)
        self.assertEqual (2, quotient.d)

    def subtractingbigvalues (self):
        frac1 = Rational(5, 2)
        frac2 = Rational(10000000,2)

        quotient = frac1.__sub__(frac2)

        self.assertEqual (-9999995, quotient.n)
        self.assertEqual (2, quotient.d)

    def subtractingfrombigvalues(self):
        frac1 = Rational(100000000, 1)
        frac2 = Rational(1,1)

        quotient = frac1.__sub__(frac2)

        self.assertEqual (99999999, quotient.n)
        self.assertEqual (1, quotient.d)
import unittest
from Modules.Rational import Rational
# Written by: Alexandru Bozdog

class DivTests(unittest.TestCase):

    fac1 = Rational()
    frac2 = Rational()
    quotient = Rational()

    def equaldivision(self):
        frac1 = Rational(5, 5)
        frac2 = Rational(6, 6)

        quotient = frac1.__sub__(frac2)

        self.assertEqual(0, quotient.n)
        self.assertEqual(1, quotient.d)

    def testsubtractingnegative(self):
        frac1 = Rational(2, 5)
        frac2 = Rational(-6, 10)

        quotient = frac1.__sub__(frac2)

        self.assertEqual(0, quotient.n)
        self.assertEqual(1, quotient.d)

    def testtopnumberchangeonly(self):
        frac1 = Rational(3, 5)
        frac2 = Rational(2, 5)

        quotient = frac1.__sub__(frac2)

        self.assertEqual(0, quotient.n)
        self.assertEqual(1, quotient.d)

    def bottomnumberchangeonly(self):
        frac1 = Rational(1, 10)
        frac2 = Rational(1, 5)

        quotient = frac2.__sub__(frac1)

        self.assertEqual(1, quotient.n)
        self.assertEqual(10, quotient.d)

    def subtractingzerovalue(self):
        frac1 = Rational(5, 2)
        frac2 = Rational(0,100)

        quotient = frac1.__sub__(frac2)

        self.assertEqual (5, quotient.n)
        self.assertEqual (2, quotient.d)

    def subtractingbigvalues (self):
        frac1 = Rational(5, 2)
        frac2 = Rational(10000000,2)

        quotient = frac1.__sub__(frac2)

        self.assertEqual (-9999995, quotient.n)
        self.assertEqual (2, quotient.d)

    def subtractingfrombigvalues(self):
        frac1 = Rational(100000000, 1)
        frac2 = Rational(1,1)

        quotient = frac1.__sub__(frac2)

        self.assertEqual (99999999, quotient.n)
        self.assertEqual (1, quotient.d)
