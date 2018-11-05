from play import print_results
import unittest


class TestPrintResults(unittest.TestCase):
    def test_check_empty(self):
        number = ''
        computer = 1
        self.assertIsNone(print_results(computer, number))

    def test_check_None(self):
        number = None
        computer = 1
        self.assertIsNone(print_results(computer, number))

    def test_check_zero(self):
        number = 0
        computer = 3
        self.assertIsNone(print_results(computer, number))


if __name__ == '__main__':
    unittest.main()