import unittest
from src import analyse


class TestAnalyse(unittest.TestCase):

    def test_check_even(self):
        self.assertEqual(analyse.check_even(([0, 154],)), [True, True])
        self.assertEqual(analyse.check_even(([-1, -2],)), [False, True])
        self.assertEqual(analyse.check_even(([-10, 20],)), [True, True])

    def test_check_palin(self):
        self.assertEqual(analyse.check_palin((['malayalam', 'foof'],)), [True, True])
        self.assertEqual(analyse.check_palin((['-+-', '/=/'],)), [True, True])
        self.assertEqual(analyse.check_palin((['nenen', 'popi'],)), [True, False])

    def test_fibonacci(self):
        self.assertEqual(analyse.fibonacci(([1, 154],)), [1, 68330027629092351019822533679447])
        self.assertEqual(analyse.fibonacci(([0, 99],)), [0, 218922995834555169026])
        self.assertEqual(analyse.fibonacci(([2, 3],)), [1, 2])

    def test_bubble_sort(self):
        self.assertEqual(analyse.bubble_sort(([[1, -154], ],)), [[-154, 1], ])
        self.assertEqual(analyse.bubble_sort(([[0, -154, 12], [12, 34, 4]],)), [[-154, 0, 12], [4, 12, 34]])
        self.assertEqual(analyse.bubble_sort(([[-1221], ],)), [[-1221], ])
        self.assertEqual(analyse.bubble_sort(([[0, 0, 0, 0], ],)), [[0, 0, 0, 0], ])

if __name__ == "__main__":
    unittest.main()
