import unittest

from programy.utils.nlp.ngrams import NGramsCreator


class NGramsCreatorTests(unittest.TestCase):

    def test_get_ngrams_3(self):
        creator = NGramsCreator()
        ngrams = creator.get_ngrams("Now is better than never.")
        self.assertIsNotNone(ngrams)
        self.assertEquals([['Now', 'is', 'better'], ['is', 'better', 'than'], ['better', 'than', 'never']], ngrams)
