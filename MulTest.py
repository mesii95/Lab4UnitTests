#Andy Thompson's Fraction Multiplication Tests
#Based on Michael Schroeder's format

import unittest
import random
from Modules.Rational import Rational

class MulTests(unittest.TestCase):
		
	def testSame(self):
		fraction1 = Rational(9,9)
		fraction2 = Rational(9,9)
		product = fraction1.__mul__(fraction2)
		self.assertEqual(1, product.n)
		self.assertEqual(1, product.d)
		
	def testZeroFormer(self):
		fraction1 = Rational(0,1)
		fraction2 = Rational(1,1)
		product = fraction1.__mul__(fraction2)
		self.assertEqual(0, product.n)
		self.assertEqual(1, product.d)
	
	# def testZeroLatter(self):
		# fraction1 = Rational(1,1)
		# fraction2 = Rational(0,1)
		# product = fraction1.__mul__(fraction2)
		# self.assertEqual(0, product.n)
		# self.assertEqual(1, product.d)
		
	def testWholeNumberOne(self):
		fraction1 = Rational(6,6)
		fraction2 = Rational(9,9)
		product = fraction1.__mul__(fraction2)
		self.assertEqual(1, product.n)
		self.assertEqual(1, product.d)
		
	def testFractionWithTwoNegatives(self):
		fraction1 = Rational(-6,-6)
		fraction2 = Rational(9,12)
		product = fraction1.__mul__(fraction2)
		self.assertEqual(9, product.n)
		self.assertEqual(12, product.d)
	
	def testFractionNegative(self):
		fraction1 = Rational(-6,6)
		fraction2 = Rational(9,12)
		product = fraction1.__mul__(fraction2)
		#I am not sure if product.n or product.d holds the negative value of the resulting fraction
			#to combat this, I check if the resulting fraction is negative, then check the absolute value of the numbers
		realProduct = product.n / product.d
		self.assertEqual(realProduct<0, true)
		self.assertEqual(abs(3), product.n)
		self.assertEqual(abs(4), product.d)
		
	def testNegativeDenominator(self):
		fraction1 = Rational(-6,1)
		fraction2 = Rational(1,1)
		product = fraction1.__mul__(fraction2)
		#Makes sure that the negative is in the numerator, as agreed upon on Feb. 17th, 2019, at 6:30pm
		self.assertNotEqual(6, product.n)
		self.assertNotEqual(-1, product.d)
		self.assertEqual(-6, product.n)
		self.assertEqual(1, product.d)
	
	def testRandom(self):
		#Might cause problems if you don't know what the random numbers are...
		for x in range(0,20):
			top1 = random.randint(-1000000,1000000)
			bot1 = random.randint(1,1000000)
			top2 = random.randint(-1000000,1000000)
			bot2 = random.randint(1,1000000)
			fraction1 = Rational(top1, bot1)
			fraction2 = Rational(top2, bot2)
			product = fraction1.__mul__(fraction2)
			self.assertEqual(top1*top2, product.n)
			self.assertEqual(bot1*bot2, product.d)
    
	# def testLargerFormerFraction(self):
		# fraction1 = Rational(10,5)
		# fraction2 = Rational(1,2)
		# product = fraction1.__mul__(fraction2)
		# self.assertEqual(10, product.n)
		# self.assertEqual(10, product.d)
		
	# def testLargerLatterFraction(self):
		# fraction1 = Rational(1,3)
		# fraction2 = Rational(4,2)
		# product = fraction1.__mul__(fraction2)
		# self.assertEqual(4, product.n)
		# self.assertEqual(6, product.d)
