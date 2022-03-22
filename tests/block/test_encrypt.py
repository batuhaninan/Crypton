import unittest
import string
import numpy as np

from crypton.block import encrypt


class TestBlockEncrypt(unittest.TestCase):
    def test_sefa(self):
        space = string.ascii_lowercase
        a = np.array([[2, 3], [3, 5]])
        b = np.array([[13], [10]])

        encrypted_text = encrypt("sefa", a, b, space)

        self.assertEqual(encrypted_text, "jgxz")

    def test_kitapx(self):
        space = string.ascii_lowercase
        a = np.array([[7, 4], [5, 3]])
        b = np.array([[10], [8]])

        encrypted_text = encrypt("kitapx", a, b, space)

        self.assertEqual(encrypted_text, "ienzzw")

    def test_para(self):
        space = string.ascii_lowercase
        a = np.array([[5, 6], [2, 3]])
        b = np.array([[8], [7]])

        encrypted_text = encrypt("para", a, b, space)

        self.assertEqual(encrypted_text, "flpp")

    def test_homework(self):
        space = string.ascii_lowercase
        a = np.array([[5, 7], [2, 3]])
        b = np.array([[11], [13]])

        encrypted_text = encrypt("stopxglobalykqrmingz", a, b, space)

        self.assertEqual(encrypted_text, "aceimzizqpadrdyfmqiw")


if __name__ == "__main__":
    unittest.main()
