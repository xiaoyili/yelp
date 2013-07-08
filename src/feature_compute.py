import numpy
import json
from loadPICKLE import load_b_train
#from bStats import get_vals_from_varname




def compute_attr1_avg_attr2(attr1_name,attr2_name,dict_name):
    attr1_list = []
    for dict_id in dict_name.keys():
        attr1_list.append(getattr(dict_name[dict_id],attr1_name))

    attr1_diff = set(attr1_list)

    attr1_dict = {}
    for attr1 in attr1_diff:
        attr1_dict[attr1] = 0

    for attr1 in attr1_diff:
        for b_id in dict_name.keys():
            if getattr(dict_name[b_id],attr1_name) is attr1:
                attr1_dict[attr1] = attr1_dict[attr1] + getattr(dict_name[b_id],attr2_name)
        attr1_dict[attr1] = attr1_dict[attr1] / attr1_list.count(attr1)

    return attr1_dict

if __name__ == "__main__":
    b_train_dict = load_b_train()

    number_dict = compute_attr1_avg_attr2('city','stars',b_train_dict)
    print number_dict
