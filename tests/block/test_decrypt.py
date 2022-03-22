import unittest
import string
import numpy as np

from crypton.block import decrypt


class TestBlockDecrypt(unittest.TestCase):
    def test_sefa(self):
        space = string.ascii_lowercase
        a = np.array([[2, 3], [3, 5]])
        b = np.array([[13], [10]])

        decrypted_text = decrypt("jgxz", a, b, space)

        self.assertEqual(decrypted_text, "sefa")

    def test_kitapx(self):
        space = string.ascii_lowercase
        a = np.array([[7, 4], [5, 3]])
        b = np.array([[10], [8]])

        decrypted_text = decrypt("ienzzw", a, b, space)

        self.assertEqual(decrypted_text, "kitapx")

    def test_para(self):
        space = string.ascii_lowercase
        a = np.array([[5, 6], [2, 3]])
        b = np.array([[8], [7]])

        decrypted_text = decrypt("flpp", a, b, space)

        self.assertEqual(decrypted_text, "para")

    def test_homework(self):
        space = string.ascii_lowercase
        a = np.array([[5, 7], [2, 3]])
        b = np.array([[11], [13]])

        decrypted_text = decrypt("aceimzizqpadrdyfmqiw", a, b, space)

        self.assertEqual(decrypted_text, "stopxglobalykqrmingz")
