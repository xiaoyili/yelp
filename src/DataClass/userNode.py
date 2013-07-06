__author__ = 'eric'

from baseNode import baseNode
from Review import Review


class userNode(baseNode):
    """
    class for user graph
    """

    def __init__(self,
                 id=None,
                 name=None,
                 review_count=None,
                 avg_stars=None,
                 votes=None):
        baseNode.__init__(self, id=id, name=name)
        self.review_count = review_count
        self.avg_stars = avg_stars
        self.votes = votes
        self.reviews = list()

    def add_reviews(self, review=None):
        """
        add reviews made by this user
        """
        assert isinstance(review, Review)
        self.reviews.append(review)


if __name__ == '__main__':
    n1 = userNode(id='0')
    n1.add_incoming(id='1')
    n1.add_incoming(id='1')
    n1.add_outgoing(id='2')
    n1.add_outgoing(id='2')
    n1.print_linkage()
    a = Review()
    n1.add_reviews(a)

