# coding=utf-8
import unittest

from zero import deep_get


DICT1 = {
    'a': 1,
    'b': 'lol',
    'c': [
        123,
        'abc',
    ],
    'd': {
        'aa': {
            'aaa': 123,
        },
        'bb': 10,
    },
}


class Tests(unittest.TestCase):

    def test_navigate_correct_value(self):
        path = ['d', 'aa', 'aaa']
        value = deep_get(DICT1, path)
        self.assertEqual(value, 123)

    def test_navigate_correct_value_short_path(self):
        path = ['d']
        value = deep_get(DICT1, path)
        self.assertEqual(value, {'aa': {'aaa': 123}, 'bb': 10})

    def test_navigate_correct_value_short_path_simple_value(self):
        path = ['b']
        value = deep_get(DICT1, path)
        self.assertEqual(value, 'lol')

    def test_navigate_correct_value_with_list_index(self):
        path = ['c', 0]
        value = deep_get(DICT1, path)
        self.assertEqual(value, 123)

    def test_navigate_correct_value_with_negative_list_index(self):
        path = ['c', -1]
        value = deep_get(DICT1, path)
        self.assertEqual(value, 'abc')

    def test_navigate_returns_none_with_list_index_out_of_range(self):
        path = ['c', 2]
        value = deep_get(DICT1, path)
        self.assertEqual(value, None)

    def test_navigate_returns_none_with_negative_list_index_out_of_range(self):
        path = ['c', -3]
        value = deep_get(DICT1, path)
        self.assertEqual(value, None)

    def test_navigate_returns_none_with_incorrect_path(self):
        path = ['b', 'aa', 'aaa']
        value = deep_get(DICT1, path)
        self.assertEqual(value, None)


"""
Allow for these test cases to be run from the command line
via `python test_addict.py`
"""
if __name__ == '__main__':
    all_tests = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(all_tests)