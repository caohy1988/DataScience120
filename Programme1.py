#!/usr/bin/env python
# encoding: utf-8
# Author: Haiyuan Cao
# Write a function to calculate all possible assignment vectors of 2n users, where n users are assigned to group 0 (control), and n users are assigned to group 1 (treatment).

import itertools
def split_user(users_list):
    users = set(users_list)
    for comb in itertools.combinations(users, int(len(users_list)/2)):
        control = set(comb)
        treatment = users - control
        yield control, treatment

users_list = [1,2,3,4,5,6,7,8]
for control, treatment in split_user(users_list):
    print (control, treatment)


