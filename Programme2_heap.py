#!/usr/bin/env python
# encoding: utf-8
# Author: Haiyuan Cao
# Given a list of tweets, determine the top 10 most used hashtags.
# Top K frequent items in the list
# Running time O(n*log(k))
import heapq
import collections

class Solution(object):
    def top_k_frequent(self, num_list, k):
        n = len(num_list)
        count_dict = collections.defaultdict(int)
        for num in num_list:
            count_dict[num] += 1

        heap = [(-value, key) for key,value in count_dict.items()]
        largest = heapq.nsmallest(k, heap)
        largest = [key for (value, key) in largest]
        return largest

num_list = [1,2,3,1,3,2,2,2,3,1,2,2,2,3,4,5]
k = 3
solution = Solution()
print (solution.top_k_frequent(num_list, k))


