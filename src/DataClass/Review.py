__author__ = 'eric'

import string
import collections


class Review(object):
    """
    review class
    """

    def __init__(self, star=None, votes=None, date=None, text=None, AFINN_dict=None):
        self.star = star
        self.votes = votes
        self.date = date
        self.AFINN_score = self.add_AFINN_score(text, AFINN_dict)


    def get_identifier(self):
        """
        get finger-print of this review, for duplicate elimination
        """
        pass


    def add_AFINN_score(self, text=None, AFINN_dict=None):
        """
        add score calculated using AFINN toolbox
        """

        # preprocessing the text
        for symbol in string.punctuation:
            if symbol != '\'':
                text = text.replace(symbol, ' ')
        words = text.lower().split()

        # getting scores from AFINN_dict
        scores = map(lambda word: AFINN_dict.get(word, 0), words)
        # getting the score feature vector
        sent_words_num = sum([score != 0 for score in scores])
        if sent_words_num > 0:
            cnt = collections.Counter(scores)
            return [cnt[score] / float(sent_words_num) for score in range(-5, 0) + range(1, 6)]
        else:
            return [0] * 10