import unittest

def factorial(n):
    return 1 if n < 1 else n * factorial(n-1)

class tester (unittest.TestCase):
	print("unitarias ")
	def test_1(self):
		self.assertEqual(1, factorial(1))

if __name__ == "__main__":
    unittest.main()