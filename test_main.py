import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(2,3) == 5
        assert add(-1,1) == 0
