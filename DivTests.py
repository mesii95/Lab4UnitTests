import unittest
from Modules.Rational import Rational

class DivTests(unittest.TestCase):
    
    fac1 = Rational()
    frac2 = Rational()
    quotient = Rational()
    
    def testGreaterDividend(self):
        frac1 = Rational(4, 5)
        frac2 = Rational(1, 6)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(24, quotient.n)
        self.assertEqual(5, quotient.d)
        
    def testGreaterDivisor(self):
        frac1 = Rational(2, 5)
        frac2 = Rational(6, 7)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(7, quotient.n)
        self.assertEqual(15, quotient.d)
        
    def testEqual(self):
        frac1 = Rational(3, 5)
        frac2 = Rational(3, 5)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(1, quotient.n)
        self.assertEqual(1, quotient.d)
        
    def testZeroDividend(self):
        frac1 = Rational(0, 0)
        frac2 = Rational(1, 5)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(0, quotient.n)
        self.assertEqual(0, quotient.d)
        
    def testZeroDivisor(self):
        frac1 = Rational(1, 6)
        frac2 = Rational(0, 1)
        
        with self.assertRaises(ValueError):
            frac1.__div__(frac2)
            
            
    def testWholeNumberBoth(self):
        frac1 = Rational(5, 5)
        frac2 = Rational(2, 2)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(1, quotient.n)
        self.assertEqual(1, quotient.d)
            
    def testWholeNumberDividend(self):
        frac1 = Rational(4, 4)
        frac2 = Rational(1, 3)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(3, quotient.n)
        self.assertEqual(1, quotient.d)
        
        
    def testWholeNumberDivisor(self):
        frac1 = Rational(3, 4)
        frac2 = Rational(6, 6)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(3, quotient.n)
        self.assertEqual(4, quotient.d)
        
        
    def testBigOverSmall(self):
        frac1 = Rational(6542, 5456)
        frac2 = Rational(1, 7)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(22897, quotient.n)
        self.assertEqual(2728, quotient.d)
        
    
    def testSmallOverBig(self):
        frac1 = Rational(3, 4)
        frac2 = Rational(6234, 4345)
        
        quotient = frac1.__div__(frac2)
        
        self.assertEqual(4345, quotient.n)
        self.assertEqual(8312, quotient.d)
        
        
    def testNegatives(self):
        frac1 = Rational(-1, 3)
        frac2 = Rational(1, -4)
        frac3 = Rational(-2, -5)
        frac4 = Rational(3, 2)
        
        quotient = frac1.__div__(frac2)
        self.assertEqual(4, quotient.n)
        self.assertEqual(3, quotient.d)
        
        quotient = frac1.__div__(frac3)
        self.assertEqual(-5, quotient.n)
        self.assertEqual(6, quotient.d)
        
        quotient = frac2.__div__(frac3)
        self.assertEqual(-5, quotient.n)
        self.assertEqual(8, quotient.d)
        
        quotient = frac1.__div__(frac4)
        self.assertEqual(-2, quotient.n)
        self.assertEqual(9, quotient.d)
        
        quotient = frac2.__div__(frac4)
        self.assertEqual(-1, quotient.n)
        self.assertEqual(6, quotient.d)
        
        quotient = frac3.__div__(frac4)
        self.assertEqual(4, quotient.n)
        self.assertEqual(15, quotient.d)
        
        
        # inverse
        
        
        quotient = frac2.__div__(frac1)
        self.assertEqual(3, quotient.n)
        self.assertEqual(4, quotient.d)
        
        quotient = frac3.__div__(frac1)
        self.assertEqual(-6, quotient.n)
        self.assertEqual(5, quotient.d)
        
        quotient = frac3.__div__(frac2)
        self.assertEqual(-8, quotient.n)
        self.assertEqual(5, quotient.d)
        
        quotient = frac4.__div__(frac1)
        self.assertEqual(-9, quotient.n)
        self.assertEqual(2, quotient.d)
        
        quotient = frac4.__div__(frac2)
        self.assertEqual(-6, quotient.n)
        self.assertEqual(1, quotient.d)
        
        quotient = frac4.__div__(frac3)
        self.assertEqual(15, quotient.n)
        self.assertEqual(4, quotient.d)
            
            
    
    
    
