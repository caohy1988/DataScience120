#!/usr/bin/env python
# encoding: utf-8
class Solution:
    # @param A : integer
    # @return an integer
    from math import *
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A

        else:
            start = 1
            end = A
            while start <= end:
                mid = (start + end) / 2
                if mid * mid == A:
                    return mid
                if mid * mid < A:
                    start = mid + 1
                    ans = mid
                else:
                    end = mid - 1


            return ans
