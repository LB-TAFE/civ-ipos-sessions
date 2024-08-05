import unittest
from src.add import add

class TestAdd(unittest.TestCase):
    def test_add_raises_type_error(self):
        with self.assertRaises(TypeError):
            add("", 1)
            add(-1, "")