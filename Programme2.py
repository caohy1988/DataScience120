#!/usr/bin/env python
# encoding: utf-8
# Author: Haiyuan Cao
# Given a list of tweets, determine the top 10 most used hashtags.
# Top K frequent items in the list

import collections

class Solution(object):
    def top_k_frequent(self, num_list, k):
        n = len(num_list)
        count_dict = collections.defaultdict(int)
        for num in num_list:
            count_dict[num] += 1

        freq_list = [[] for x in range(n+1)]
        for key in count_dict:
            freq_list[count_dict[key]].append(key)
        ans = []
        for i in range(n, 0, -1):
            ans.append(freq_list[i])
        result = [item for sublist in ans for item in sublist]
        return result[:k]

num_list = [1,2,3,1,3,2,2,2,3,1,2,2,2,3,4,5]
k = 3
solution = Solution()
print (solution.top_k_frequent(num_list, k))


