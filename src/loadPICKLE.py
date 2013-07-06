__author__ = 'dv'

"""
load pickled data
"""
import gzip
import cPickle
import os

root = "/Volumes/HDD750/home/DATA/yelp_data/pickledData"

b_train_fn = os.path.join(root, "b_train.pkl.gz")
u_train_fn = os.path.join(root, "u_train.pkl.gz")
b_test_fn = os.path.join(root, "b_test.pkl.gz")
u_test_fn = os.path.join(root, "u_test.pkl.gz")


def load_pickle(filename):
    file = gzip.GzipFile(filename, 'rb')
    dict = cPickle.load(file)
    file.close()
    return dict


def load_b_train():
    return load_pickle(b_train_fn)


def load_u_train():
    return load_pickle(u_train_fn)


def load_b_test():
    return load_pickle(b_test_fn)


def load_u_test():
    return load_pickle(u_test_fn)


if __name__ == '__main__':
    print "... loading business train data"
    # read b_train.pkl.gz
    b_train_dict = load_b_train()
    # print b_train_dict['yDnRf8m_YI4AXHVGH6-fuQ'].reviews[0].AFINN_score
    print len(b_train_dict)

    print "... loading user train data"
    # # read u_train.pkl.gz
    u_train_dict = load_u_train()
    # print b_train_dict['yDnRf8m_YI4AXHVGH6-fuQ'].reviews[0].AFINN_score
    print len(u_train_dict)

    print "... loading business test data"
    # read b_test.pkl.gz
    b_test_dict = load_b_test()
    print len(b_test_dict)

    print "... loading user test data"
    # # read u_test.pkl.gz
    u_test_dict = load_u_test()
    print len(u_test_dict)