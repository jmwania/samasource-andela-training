import unittest
from sum import sum
class testsum(unittest.TestCase):
	"""sum of two numbers test cases"""
	def test_sum(self):
		self.assertEqual(5+4,9)
	#just an example test to test type of variable.
	def test_type(self):
		self.assertTrue(type(5) is int)

if __name__ == '__main__':
	unittest.main()