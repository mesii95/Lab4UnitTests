import unittest
from Modules.Rational import Rational

class Test__str__(unittest.TestCase):
    frac = Rational()
    def test_int_normal(self):
        frac = Rational(3, 4)
        self.assertEqual(frac.__str__(), "3/4")
    def test_int_normal_2(self):
        frac = Rational(1, 1)
        self.assertEqual(frac.__str__(), "1/1")
    def test_int_large_reduction(self):
        frac = Rational(-999, 999)
        self.assertEqual(frac.__str__(), "-1/1")
    def test_int_small_incretion(self):
        frac = Rational(.01/.0001)
        self.assertEqual(frac.__str__(), "100/1")
    def test_int_large_strings(self):
        x = "1"
        for i in range(100):
            x += x
            i += 1
        frac = Rational(x, 3)
        self.assertEqual(frac.__str__(), x+"/3")
    def test_str_no_inproper_strings(self):
        frac = Rational("yes", "no")
        with self.assertRaises(Exception, msg="No, bad program, get off the couch"):
            frac.__str__()
    def test_str_strings_to_ints(self):
        frac = Rational("34", "22")
        self.assertEqual(frac.__str__(), "17/11")
    def test_str_no_objects(self):
        frac = Rational(object, object)
        with self.assertRaises(Exception, msg="No, bad program, get off the couch"):
            frac.__str__()
