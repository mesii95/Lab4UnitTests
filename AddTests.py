import unittest
from Modules.Rational import Rational


class AddTests(unittest.TestCase):
    fac1 = Rational()
    frac2 = Rational()
    product = Rational()

    def testAddZero(self):
        frac1 = Rational(4, 5)
        frac2 = Rational(0, 1)

        product = frac1.__add__(frac2)

        self.assertEqual(4, product.n)
        self.assertEqual(5, product.d)

    def testAddNegative(self):
        frac1 = Rational(4, 5)
        frac2 = Rational(-3, 5)

        product = frac1.__add__(frac2)

        self.assertEqual(1, product.n)
        self.assertEqual(5, product.d)

    def testAddLarge(self):
        frac1 = Rational(3, 1)
        frac2 = Rational(1000000, 1)

        product = frac1.__add__(frac2)

        self.assertEqual(1000003, product.n)
        self.assertEqual(1, product.d)

    def testAddSmall(self):
        frac1 = Rational(1, 100000)
        frac2 = Rational(1, 5)

        product = frac1.__add__(frac2)

        self.assertEqual(20001, product.n)
        self.assertEqual(10000, product.d)

    def testWholeNumber(self):
        frac1 = Rational(1, 1)
        frac2 = Rational(5, 1)

        product = frac1.__add__(frac2)

        self.assertEqual(6, product.n)
        self.assertEqual(1, product.d)

    def testOneWholeNumber(self):
        frac1 = Rational(5, 5)
        frac2 = Rational(3, 2)

        product = frac1.__add__(frac2)

        self.assertEqual(5, product.n)
        self.assertEqual(2, product.d)

    def testNegativeSolution(self):
        frac1 = Rational(-4, 1)
        frac2 = Rational(7, 3)

        product = frac1.__add__(frac2)

        self.assertEqual(-5, product.n)
        self.assertEqual(3, product.d)

    def testZeroPlusZero(self):
        frac1 = Rational(0, 4)
        frac2 = Rational(0, 4)

        product = frac1.__add__(frac2)

        self.assertEqual(0, product.n)
        self.assertEqual(4, product.d)

    def testTwoBig(self):
        frac1 = Rational(123456789, 3)
        frac2 = Rational(987654321, 4)

        product = frac1.__add__(frac2)

        self.assertEqual(1152263373, product.n)
        self.assertEqual(4, product.d)

    def testTwoSmall(self):
        frac1 = Rational(3, 123456789)
        frac2 = Rational(3, 987654321)

        product = frac1.__add__(frac2)

        self.assertEqual(123456790, product.n)
        self.assertEqual(4516023374542047, product.d)



