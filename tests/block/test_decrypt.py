import unittest
import string
import numpy as np

from crypton.block import encrypt, decrypt


class TestBlockDecrypt(unittest.TestCase):
	def test_sefa(self):
		space = string.ascii_lowercase
		A = np.array([[2,3],[3,5]])
		B = np.array([[13],[10]])
		crypted_text = encrypt("sefa", A, B, space)
		decrypted_text = decrypt(crypted_text, A, B, space)
		
		self.assertEqual(
			decrypted_text, "sefa"
		)

	def test_kitapx(self):
		space = string.ascii_lowercase
		A = np.array([[7,4],[5,3]])
		B = np.array([[10],[8]])
		crypted_text = encrypt("kitapx", A, B, space)
		decrypted_text = decrypt(crypted_text, A, B, space)
		
		self.assertEqual(
			decrypted_text, "kitapx"
		)

	def test_para(self):
		space = string.ascii_lowercase
		A = np.array([[5, 6], [2, 3]])
		B = np.array([[8],[7]])
		crypted_text = encrypt("para", A, B, space)
		decrypted_text = decrypt(crypted_text, A, B, space)
		
		self.assertEqual(
			decrypted_text, "para"
		)

	def test_homework(self):
		space = string.ascii_lowercase
		A = np.array([[5, 7], [2, 3]])
		B = np.array([[11],[13]])
		decrypted_text = decrypt("aceimzizqpadrdyfmqiw", A, B, space)
		
		self.assertEqual(
			decrypted_text, "stopxglobalykqrmingz"
		)


if __name__ == "__main__":
	unittest.main()
