__author__ = 'eric'

import numpy as np
from sklearn import grid_search
from sklearn import cross_validation as cv
from sklearn.svm import SVC
# from sklearn.decomposition import PCA
from sklearn.decomposition import PCA
from sklearn.ensemble import AdaBoostClassifier

from sklearn.cross_validation import StratifiedKFold

<<<<<<< HEAD
workDir = '/home/Desktop/DATA/'
=======
workDir = '/home/Desktop/Data/'
>>>>>>> a1754e2bcf547d007ff11720f9666576a7a746d7

# Read data
print '... loading data'
train = np.genfromtxt(open(workDir + 'train.csv', 'rb'), delimiter=',')
labels = np.genfromtxt(open(workDir + 'trainLabels.csv', 'rb'), delimiter=',')
test = np.genfromtxt(open(workDir + 'test.csv', 'rb'), delimiter=',')


# print '... whitening training & testing data'
pca = PCA(n_components=12, whiten=True)
train = pca.fit_transform(train)
test = pca.transform(test)

# # for SVM model parameters
# print '... SVM C and gamma ... 1'
# C_range = 10.0 ** np.arange(7, 10)
# gamma_range = 10.0 ** np.arange(-4, 0)
# params = dict(gamma=gamma_range, C=C_range)
# cvk = StratifiedKFold(labels, n_folds=3)
# classifier = SVC()
# clf = grid_search.GridSearchCV(classifier, param_grid=params, cv=cvk)
# clf.fit(train, labels)
# print("The best classifier is: ", clf.best_estimator_)
#
# print '... SVM C and gamma ... 2'
# C_range = 10.0 ** np.arange(6.5, 7.5, .25)
# gamma_range = 10.0 ** np.arange(-1.5, 0.5, .25)
# params = dict(gamma=gamma_range, C=C_range)
# cvk = StratifiedKFold(labels, n_folds=3)
# classifier = SVC()
# clf = grid_search.GridSearchCV(classifier, param_grid=params, cv=cvk)
# clf.fit(train, labels)
# print("The best classifier is: ", clf.best_estimator_)


# for Ada
clf = AdaBoostClassifier(n_estimators=10000)
scores = cv.cross_val_score(clf, train, labels)



# Estimate score
# scores = cv.cross_val_score(clf.best_estimator_, train, labels, cv=30)
print('Estimated score: %0.5f (+/- %0.5f)' % (scores.mean(), scores.std() / 2))

# # Predict and save
# result = clf.best_estimator_.predict(test)
#
# np.savetxt(workDir + 'result.csv', result, fmt='%d')

