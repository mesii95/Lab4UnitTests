import unittest
from Modules.Rational import Rational


class Rational(unittest.TestCase):
    
    def testDefault(self):
        frac = Rational()
        
        self.assertEqual(0, frac.n)
        self.assertEqual(1, frac.d)
        
        
    def testNormalizeNegatives(self):
        
        frac1 = Rational(-1, 3)
        self.assertEqual(-1, frac1.n)
        self.assertEqual(3, frac1.d)
        
        frac2 = Rational(1, -4)
        self.assertEqual(-1, frac1.n)
        self.assertEqual(4, frac1.d)
        
        frac3 = Rational(-2, -5)
        self.assertEqual(2, frac1.n)
        self.assertEqual(5, frac1.d)
        
    
    def testString(self):
        
        with self.assertRaises(TypeError):
            Rational("hello", 1)
            
        with self.assertRaises(TypeError):
            Rational(1, "hello")
            
        with self.assertRaises(TypeError):
            Rational("hello", "hello")
            
        with self.assertRaises(TypeError):
            Rational("123", 1)
            
        with self.assertRaises(TypeError):
            Rational(1, "23")
            
        with self.assertRaises(TypeError):
            Rational("122", "1565")
            
    
    def testBoolean(self):
        
        with self.assertRaises(TypeError):
            Rational(True, 1)
            
        with self.assertRaises(TypeError):
            Rational(1, False)
            
        with self.assertRaises(TypeError):
            Rational(False, True)
            
    
    def testObject(self):
        
        class Ob:
            def __init__(self):
                data = None
                
        ob = Ob()
        
        with self.assertRaises(TypeError):
            Rational(ob, 1)
            
        with self.assertRaises(TypeError):
            Rational(1, ob)
            
        with self.assertRaises(TypeError):
            Rational(ob, ob)
            
            
    def testList(self):
        
        list = [1, 2, 3]
        
        with self.assertRaises(TypeError):
            Rational(list, 1)
            
        with self.assertRaises(TypeError):
            Rational(1, list)
            
        with self.assertRaises(TypeError):
            Rational(list, list)
            
            
    def testFloat(self):
        
        with self.assertRaises(TypeError):
            Rational(4.5, 1)
            
        with self.assertRaises(TypeError):
            Rational(1, 3.445)
            
        with self.assertRaises(TypeError):
            Rational(12.213, 123.4366)
            
            
    def testTruple(self):
        
        truple = ('123', 2, True)
        
        with self.assertRaises(TypeError):
            Rational(truple, 1)
            
        with self.assertRaises(TypeError):
            Rational(1, truple)
            
        with self.assertRaises(TypeError):
            Rational(truple, truple)
            
            
    def testDictionary(self):
        
        d = {}
        
        with self.assertRaises(TypeError):
            Rational(d, 1)
            
        with self.assertRaises(TypeError):
            Rational(1, d)
            
        with self.assertRaises(TypeError):
            Rational(d, d)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
