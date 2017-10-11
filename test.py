import unittest
from sum import sum
class testsum(unittest.TestCase):
	"""sum of two numbers test cases"""
	def test_sum(self):
		self.assertEqual(sum(5,4),9)

	def test_is_not_string(self):
		self.assertRaises(TypeError, sum(5,'we'))
		
if __name__ == '__main__':
	unittest.main()