#!/usr/bin/env python
# encoding: utf-8
# Author: Haiyuan Cao
# 0-1 Knapsack problem

class Solution(object):
    def knapsack(self, value, weight, weight_limit):
        index_1 = 0
        index_2 = 0
        length_list = len(value)
        value_matrix = [[0 for i in range(weight_limit+1) ] for j in range(length_list)]

        for index_1 in range(length_list):
            for index_2 in range(weight_limit+1):
                if weight[index_1] > index_2:
                    value_matrix[index_1][index_2] = value_matrix[index_1-1][index_2]
                else:
                    value_matrix[index_1][index_2] = max(value_matrix[index_1-1][index_2], value_matrix[index_1-1][index_2-weight[index_1]] + value[index_1])
        index = 0
        max_value = value_matrix[length_list-1][weight_limit]
        weight_left = weight_limit
        list_index = []
        while index >= 0:
            while weight_left > 0:
                left_index = length_list - 1 - index
                while (value_matrix[left_index][weight_left] == value_matrix[left_index][weight_left-1]):
                    weight_left -= 1
                left_value = max_value - value[left_index]
                left_weight = weight_left - weight[left_index]
                if value_matrix[left_index-1][left_weight] == left_value:
                    max_value -= value[left_index]
                    list_index.append(left_index+1)
                    index += 1
                    weight_left -= weight[left_index]
                else:
                    index += 1
            if weight_left == 0:
                break
        return (value_matrix[length_list-1][weight_limit], list_index)

values = [1,2,3,4,5,6,7,10,11]
weight = [10,9,1,2,4,5,6,7,8]
weight_limit = 37
solution = Solution()
print (solution.knapsack(values, weight, weight_limit))
