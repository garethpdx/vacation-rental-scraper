import unittest

from scraper.parse import key_value


class DictTest(unittest.TestCase):
    def test_simple_dict(self):
        d = {'name': 'bob',
             'color': 'green'}
        self.assertEquals(key_value(d, 'color'), 'green')

    def test_nested_dict(self):
        d = {'properties': {'initial':
                            {'name': 'bob',
                             'color': 'green'},
                            'final':
                            {'name': 'frank',
                             'color': 'chartreuse'}},
             'spans': {'2017': {'february': '1d93'},
                       '2016': {'march': '9jf'}}
             }
        self.assertEquals(key_value(d, 'march'), '9jf')


if __name__ == '__main__':
    unittest.main()
