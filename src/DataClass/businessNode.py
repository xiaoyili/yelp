__author__ = 'eric'

from baseNode import baseNode
from Review import Review


class businessNode(baseNode):
    """
    business node class
    """

    def __init__(self,
                 id=None,
                 name=None,
                 neighbor=None,
                 addr=None,
                 city=None,
                 state=None,
                 lati=None,
                 longi=None,
                 stars=None,
                 review_count=None,
                 categories=None,
                 open=None):
        self.id = id
        self.name = name
        self.neighbor = neighbor
        self.addr = addr
        self.city = city
        self.state = state
        self.lati = lati
        self.longi = longi
        self.stars = stars
        self.review_count = review_count
        self.categories = categories
        self.open = open

        self.reviews = list()
        self.checkin_info = None


    def __parse_checkin_info(self):
        pass


    def add_reviews(self, review=None):
        """
        add reviews made by this user
        """
        assert isinstance(review, Review)
        self.reviews.append(review)

    def add_checkin(self, checkin=None):
        """
        add checkin dict
        """
        assert isinstance(checkin, dict)
        self.checkin_info = checkin
