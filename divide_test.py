import unittest
from divide import divide
class test_divide(unittest.TestCase):
	"""test method"""
	def test_divide(self):
		self.assertEqual(divide(9,3),3)
		self.assertEqual(divide(30,2),15)
	def test_not_divisible_by_non_digit(self):
		self.assertRaises(TypeError, divide(9,'a'))
		self.assertRaises(TypeError, divide('b','a'))
	def test_not_divisible_by_zero(self):
		try:
			divide(9,0)
		except ZeroDivisionError:
			self.fail(ZeroDivisionError)
if __name__ == "__main__":
	unittest.main()