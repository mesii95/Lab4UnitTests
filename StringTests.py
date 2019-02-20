import unittest
from Modules.Rational import Rational

class Test__str__(unittest.TestCase):
    frac = Rational()
    def test_int(self):
        frac = Rational(3, 4)
        self.assertEqual(frac.__str__(), "3/4")
    def test_int2(self):
        frac = Rational(1, 1)
        self.assertEqual(frac.__str__(), "1/1")
    def test_int3(self):
        frac = Rational(-999, 999)
        self.assertEqual(frac.__str__(), "-999/999")
    def test_int4(self):
        frac = Rational(.01/.0001)
        self.assertEqual(frac.__str__(), ".01/.0001")
    def test_int5(self):
        x = "1"
        for i in range(100):
            x += x
            i += 1
        frac = Rational(x, 2)
        self.assertEqual(frac.__str__(), x+"/2")
    def test_str(self):
        frac = Rational("yes", "no")
        with self.assertRaises(Exception, msg="No, bad program, get off the couch"):
            frac.__str__()
    def test_str2(self):
        frac = Rational("34", "22")
        self.assertEqual(frac.__str__(), "34/22")
    def test_str3(self):
        frac = Rational(object, object)
        with self.assertRaises(Exception, msg="No, bad program, get off the couch"):
            frac.__str__()
