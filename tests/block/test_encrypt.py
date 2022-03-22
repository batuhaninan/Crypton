import unittest
import string
import numpy as np

from crypton.block import encrypt


class TestBlockEncrypt(unittest.TestCase):
	def test_sefa(self):
		space = string.ascii_lowercase
		A = np.array([[2,3],[3,5]])
		B = np.array([[13],[10]])
		crypted_text = encrypt("sefa", A, B, space)
		
		self.assertEqual(
			crypted_text, "jgxz"
		)

	def test_kitapx(self):
		space = string.ascii_lowercase
		A = np.array([[7,4],[5,3]])
		B = np.array([[10],[8]])
		crypted_text = encrypt("kitapx", A, B, space)
		
		self.assertEqual(
			crypted_text, "ienzzw"
		)

	def test_para(self):
		space = string.ascii_lowercase
		A = np.array([[5, 6], [2, 3]])
		B = np.array([[8],[7]])
		crypted_text = encrypt("para", A, B, space)
		
		self.assertEqual(
			crypted_text, "flpp"
		)

	def test_homework(self):
		space = string.ascii_lowercase
		A = np.array([[5, 7], [2, 3]])
		B = np.array([[11],[13]])
		crypted_text = encrypt("stopxglobalykqrmingz", A, B, space)
		
		self.assertEqual(
			crypted_text, "aceimzizqpadrdyfmqiw"
		)


if __name__ == "__main__":
	unittest.main()
