__author__ = 'dv'

import numpy as np
import matplotlib.pyplot as plt
from loadPICKLE import load_u_train

def get_vals_from_varname(d, varname):
    return np.array([getattr(d.values()[i], varname) for i in range(len(d))])

# this decision seems to be not effective
# if 'b_train_dict' not in vars() and 'b_train_dict' not in globals():
u_train_dict = load_u_train()
    
# get stats of stars

# plot the histogram of all stars
plt.figure(1)
stars = get_vals_from_varname(u_train_dict, 'avg_stars')
pdf, bins, patches = plt.hist(stars, bins=np.arange(1,5.5,.5), normed=True)  # there are only one user who give 0 star, 
                                                                             # which should be an outlier.
print pdf/2  # this is a bug of matplotlib library, so we must dividing it by 2 to correct it

# plot the histogram of all review counts
plt.figure(2)
review_cnts = get_vals_from_varname(u_train_dict, 'review_count')
print plt.hist(review_cnts, bins=np.arange(min(review_cnts),max(review_cnts)+10,10))

# plot the histogram of review counts grouped by star
plt.figure(3)
star_intervals = np.linspace(1,5,10)
for i in range(len(star_intervals)-1):
    plt.subplot(3, 3, i+1)
    star_start = star_intervals[i]
    star_end = star_intervals[i+1]
    if i != len(star_intervals)-2:
        review_cnts_group_by_star = review_cnts[np.all([stars>=star_start, stars<star_end], axis=0)]
    else:
        review_cnts_group_by_star = review_cnts[np.all([stars>=star_start, stars<=star_end], axis=0)]
    plt.hist(review_cnts_group_by_star, bins=np.arange(min(review_cnts_group_by_star),max(review_cnts_group_by_star)+10,10))
    plt.title('Star from '+str(star_start)+' to '+str(star_end))
plt.show()
