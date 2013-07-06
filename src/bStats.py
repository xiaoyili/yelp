__author__ = 'dv'

import numpy as np
import matplotlib.pyplot as plt
from loadPICKLE import load_b_train

def get_vals_from_varname(d, varname):
    return np.array([getattr(d.values()[i], varname) for i in range(len(d))])

# this decision seems to be not effective
# if 'b_train_dict' not in vars() and 'b_train_dict' not in globals():
b_train_dict = load_b_train()
    
# get stats of stars

# plot the histogram of all stars
plt.figure(1)
stars = get_vals_from_varname(b_train_dict, 'stars')
pdf, bins, patches = plt.hist(stars, bins=np.append(np.unique(stars), np.unique(stars)[-1]+0.5)-0.25, normed=True)
print pdf/2  # this is a bug of matplotlib library, so we must dividing it by 2 to correct it

# plot the histogram of all review counts
plt.figure(2)
review_cnts = get_vals_from_varname(b_train_dict, 'review_count')
print plt.hist(review_cnts, bins=np.arange(min(review_cnts),max(review_cnts)+10,10))

# plot the histogram of review counts grouped by star
plt.figure(3)
for i, star in enumerate(np.arange(1,5.5,.5)):
    plt.subplot(3, 3, i+1)
    review_cnts_group_by_star = review_cnts[stars==star]
    plt.hist(review_cnts_group_by_star, bins=np.arange(min(review_cnts_group_by_star),max(review_cnts_group_by_star)+10,10))
    plt.title('Star: '+str(star))
plt.show()
