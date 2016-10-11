# Product of Array Except Self
# Author: Haiyuan Cao
# Date: Oct. 10, 2016

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        prod = 1
        list_temp = []
        while index < len(nums):
            list_temp.append(prod)
            prod *= nums[index]
            index += 1

        prod2 = 1
        index2 = len(nums) - 1
        while index2 >= 0:
            list_temp[index2] = list_temp[index2] * prod2
            prod2 = prod2 * nums[index2]
            index2 -= 1

        return list_temp
