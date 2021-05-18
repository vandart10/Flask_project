import unittest
from app_module import trans
from app_module import url


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(trans['convey'], 'холст')

    def test_2(self):
        self.assertEqual('https://studynow.ru/dicta/allwords', url)


if __name__ == '__main__':
    unittest.main()
