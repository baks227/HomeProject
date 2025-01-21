import unittest
import seed_data

class TestWEBsite(unittest.TestCase):
    def setUp(self):
        self.seed_data = seed_data
    def cousts_product(self):
        self.assertNotEqual(seed_data.PC.price, 0)
    def test_add(self):
        self.assertIsNotNone(seed_data.add_user('test1','tese','tee4'))

    #def test_subtract(self):
     #   self.assertEqual(self.calculator.subtract(10,5), 5)
    #def test_multiply(self):
     #   self.assertEqual(self.calculator.multiply(3,7), 21)
    #def test_divide(self):
      #  self.assertEqual(self.calculator.divide(10,2), 5)
    if __name__ == '__main__':
        unittest.main()