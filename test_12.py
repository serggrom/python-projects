
import unittest
import Part12
'''
class TestPart(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_one_word(self):
        text = 'duck'
        result = Part12.just_do_it(text)
        self.assertEqual(result, 'Duck')
    def test_multiple_word(self):
        text = 'a veritable flock of ducks'
        result = Part12.just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')
    def test_words_with_apostrophes(self):
        text = "I'm fresh out of ideas"
        result = Part12.just_do_it(text)
        self.assertEqual(result, "I'm Fresh Out Of Ideas")
    def test_words_with_quotes(self):
        text = "\"You're despicable,\" said Daffy Duck"
        result = Part12.just_do_it(text)
        self.assertEqual(result, "\"You're Despicable,\" Said Daffy Duck")
if __name__ == '__main__':
    unittest.main()
'''

from nose.tools import eq_

'''
def test_one_word():
    text = 'duck'
    result = Part12.just_do_it(text)
    eq_(result, 'Duck')
def test_multiple_word():
    text = 'a veritable flock of ducks'
    result = Part12.just_do_it(text)
    eq_(result, 'A Veritable Flock Of Ducks')
def test_words_with_apostrophes():
    text = "I'm fresh out of ideas"
    result = Part12.just_do_it(text)
    eq_(result, "I'm Fresh Out Of Ideas")
def test_words_with_quotes():
    text = "\"You're despicable,\" said Daffy Duck"
    result = Part12.just_do_it(text)
    eq_(result, "\"You're Despicable,\" Said Daffy Duck")
'''

from test_12 import dump
@dump
def double (*args, **kwargs):
    "Double every argument"
    output_list = [2 * arg for arg in args]
    output_dict = {k:2*v for k,v in kwargs.items()}
    return output_list, output_dict
if __name__ == "__main__":
    output = double(3, 5, first=100, next=98.6, last=-40)

















