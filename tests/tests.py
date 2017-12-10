import unittest

from bs4 import BeautifulSoup

from scraper.parse import nested_get
from scraper.base import TransformExtractor
from scraper.vendors.airbnb import preprocessor

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


class ExtractorTests(unittest.TestCase):

    def test_simple_extractor(self):
        s = TransformExtractor("february", nested_get)
        self.assertEqual(s.extract(NESTED_DICT), "1d93")

    def test_extractor_transform(self):
        def first_char(chars):
            return chars[0]
        s = TransformExtractor("february", nested_get, transform=first_char)
        self.assertEqual(s.extract(NESTED_DICT), "1")


class AirBNBTest(unittest.TestCase):
    def test_preprocessor(self):
        html = ("<html><body><script type='application/json' data-hypernova" +
                "-key='spaspabundlejs'>  <!--{}--></script><p>first</p><p c" +
                "lass='find'>second</p></body></html>")
        soup = BeautifulSoup(html, "html.parser")
        self.assertEqual(preprocessor(soup), dict())


if __name__ == '__main__':
    unittest.main()
