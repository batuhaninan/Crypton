import unittest
import string

from crypton.affine import decrypt


class TestAffineDecrypt(unittest.TestCase):
    def test_long_text(self):
        space = string.ascii_lowercase

        result = decrypt(
            "fmxvedkaphferbndkrxrsrefmorudsdkdvshvufedkaprkdlyevlrhhrh", 3, 5, space
        )

        self.assertEqual(
            result, "algorithmsarequitegeneraldefinitionsofarithmeticprocesses"
        )

    def test_short_word(self):
        space = string.ascii_lowercase

        result = decrypt("yvtre", 3, 5, space)

        self.assertEqual(result, "power")
