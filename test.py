import unittest
from sum import sum
class testsum(unittest.TestCase):
	"""sum of two numbers test cases"""
	def test_sum(self):
		self.assertEqual(sum(5,4),9)

	def test_string(self):
		self.assertNotEqual(sum(5,'we'), '5we')

if __name__ == '__main__':
	unittest.main()