import calc as cl
import unittest

def setUpModule():
    print('\nRunning setUpModule')

def tearDownModule():
    print('\nRunning tearDownModule')

class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nRunning setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\nRunning tearDownClass')
    
    def setUp(self):
        print('\nRunning setUpmethod')
        
    def tearDown(self):
        print('\nRunning tearDownmethod')

    def test_add(self): 
        self.assertEqual(cl.add(10, 5), 15)

    def test_add_decimal(self):
        self.assertAlmostEqual(cl.add(10.0000001, 5.0000001), 15.0000002, 7)

    #Honestly I don't think this should be valid but there's no docs that says that 
    #the function should only add number so I'm just gonna leave it here.
    def test_add_string(self):
        self.assertEqual(cl.add('Hello', ' World'), 'Hello World')

    def test_subtract(self):
        self.assertEqual(cl.subtract(10, 5), 5)

    def test_subtract_decimal(self):
        self.assertAlmostEqual(cl.subtract(10.0000001, 5.0000001), 5.0000000, 7)

    def test_subtract_float(self):
        self.assertEqual(cl.subtract(10, 5.0), 5.0)

    def test_multiply(self):
        self.assertEqual(cl.multiply(10, 5), 50)

    
    def test_multiply_decimal(self):
        self.assertAlmostEqual(cl.multiply(10.0000001, 5), 50.0000005, 7)

    def test_multiply_zero(self):
        self.assertEqual(cl.multiply(10, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(cl.divide(10, 3), 3.3333333, 7)

    def test_divide_by_negative(self):
        self.assertEqual(cl.divide(10, -2), -5)
        self.assertEqual(cl.divide(-10, -2), 5)

    def test_divide_zero(self):
        # self.assertRaises(ValueError, cl.divide, 10, 0)
        with self.assertRaises(ValueError):
            cl.divide(10, 0)

    def test_exp(self):
        self.assertEqual(cl.exp(2,2), 4)

    def test_exp_negative_expoent(self):
        self.assertEqual(cl.exp(-2,2), 0.25)

    def test_exp_zero(self):
        self.assertEqual(cl.exp(0,3000), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)