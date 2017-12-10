import unittest

from scraper.parse import nested_get
from scraper.base import TransformSelector

NESTED_DICT = {'properties':
               {'initial':
                {'name': 'bob',
                 'color': 'green'},
                'final':
                {'name': 'frank',
                 'color': 'chartreuse',
                 'code': 42,
                 'lists': [32, 53, 3]}},
               'spans': {'2017': {'february': '1d93'},
                         '2016': {'march': '9jf'}}}


class DictTest(unittest.TestCase):

    def test_simple_dict(self):
        d = {'name': 'bob',
             'color': 'green'}
        self.assertEqual(nested_get(d, 'color'), 'green')
        self.assertEqual(nested_get(d, 'orange'), None)

    def test_nested_dict(self):
        self.assertEqual(nested_get(NESTED_DICT, 'march'), '9jf')
        self.assertEqual(nested_get(NESTED_DICT, 'april'), None)


class SelectorTests(unittest.TestCase):

    def test_simple_selector(self):
        s = TransformSelector("february")
        self.assertEqual(s.parse(NESTED_DICT), "1d93")

    def test_selector_transform(self):
        def first_char(chars):
            return chars[0]
        s = TransformSelector("february", first_char)
        self.assertEqual(s.parse(NESTED_DICT), "1")


if __name__ == '__main__':
    unittest.main()
