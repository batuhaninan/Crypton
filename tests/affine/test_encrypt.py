import unittest
import string

from crypton.affine import encrypt


class TestDecrypt(unittest.TestCase):
    def test_long_text(self):
        space = string.ascii_lowercase

        result = encrypt(
            "algorithmsarequitegeneraldefinitionsofarithmeticprocesses", 3, 5, space
        )

        self.assertEqual(
            result, "fmxvedkaphferbndkrxrsrefmorudsdkdvshvufedkaprkdlyevlrhhrh"
        )

    def test_short_word(self):
        space = string.ascii_lowercase

        result = encrypt("power", 3, 5, space)

        self.assertEqual(result, "yvtre")


if __name__ == "__main__":
    unittest.main()
