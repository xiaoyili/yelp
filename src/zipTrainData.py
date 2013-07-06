__author__ = 'eric'

"""
organize training json files into two dictionaries.

"""


# std lib
import json
import gzip
import cPickle
import os

# local lib
from DataClass.businessNode import businessNode
from DataClass.userNode import userNode
from DataClass.Review import Review

root = "/Volumes/HDD750/home/DATA/yelp_data"

json_train_business = os.path.join(root, "yelp_training_set/yelp_training_set_business.json")
json_train_review = os.path.join(root, "yelp_training_set/yelp_training_set_review.json")
json_train_user = os.path.join(root, "yelp_training_set/yelp_training_set_user.json")
json_train_checkin = os.path.join(root, "yelp_training_set/yelp_training_set_checkin.json")

AFINN_fn = '../AFINN/AFINN-111.txt'

# load business
b_dict = dict()
fd = open(json_train_business)
for line in fd:
    data = json.loads(line)

    bN = businessNode(id=data['business_id'],
                      name=data['name'],
                      neighbor=data['neighborhoods'],
                      addr=data['full_address'],
                      city=data['city'],
                      state=data['state'],
                      lati=data['latitude'],
                      longi=data['longitude'],
                      stars=data['stars'],
                      review_count=data['review_count'],
                      categories=data['categories'],
                      open=data['open'])

    b_dict[data['business_id']] = bN

fd.close()
print "... business file loaded! \tTotal: " + str(len(b_dict)) + " businesses"

# load checkin
counter = 0
fd = open(json_train_checkin)
for line in fd:
    data = json.loads(line)
    counter += 1
    if data['business_id'] in b_dict.keys():
        b_dict[data['business_id']].add_checkin(data['checkin_info'])
    else:
        print "ERR... " + data['business_id'] + " not found in business dict"

print "... checkin file loaded! \tTotal: " + str(counter) + " businesses provide checkin info"
fd.close()


# load user
u_dict = dict()
fd = open(json_train_user)
for line in fd:
    data = json.loads(line)

    uN = userNode(id=data['user_id'],
                  name=data['name'],
                  review_count=data['review_count'],
                  avg_stars=data['average_stars'],
                  votes=data['votes'])

    u_dict[data['user_id']] = uN

fd.close()
print "... user file loaded! \tTotal: " + str(len(u_dict)) + " users"


# load reviews
counter = 0
N_extra_reviews = 0
fd = open(json_train_review)
AFINN_dict = dict(map(lambda (k, v): (k, int(v)),
                      [line.split('\t') for line in open(AFINN_fn)]))
for line in fd:
    data = json.loads(line)
    counter += 1
    print "... " + str(counter) + " reviews loaded"
    rV = Review(star=data['stars'],
                date=data['date'],
                votes=data['votes'],
                text=data['text'],
                AFINN_dict=AFINN_dict)

    if data['business_id'] in b_dict.keys():
        b_dict[data['business_id']].add_reviews(rV)
    else:
        print "ERR... " + data['business_id'] + " not found in business dict"

    if data['user_id'] in u_dict.keys():
        u_dict[data['user_id']].add_reviews(rV)
    else:
        # print "ERR... " + data['user_id'] + " not found in user dict"
        N_extra_reviews += 1

fd.close()
print "... review file loaded! \tTotal: " + str(counter) + " reviews provided, there are " \
      + str(N_extra_reviews) + " anonymous(or out of training set) reviews"

b_file = os.path.join(root, "pickledData/b_train.pkl.gz")
file = gzip.GzipFile(b_file, 'wb')
cPickle.dump(b_dict, file)
file.close()
print "... business dict pickled"

u_file = os.path.join(root, "pickledData/u_train.pkl.gz")
file = gzip.GzipFile(u_file, 'wb')
cPickle.dump(u_dict, file)
file.close()
print "... user dict pickled"