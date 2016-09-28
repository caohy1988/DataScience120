# Yates-Fisher Random Shuffling Algorithm

import random
class Solution(object):
    def shuffling(self, arr, number):
        end = number - 1
        for index in range(end, 0, -1):
            rand = random.randint(0, index)
            if rand == index:
                continue
            arr[rand], arr[index] = arr[index], arr[rand]
        return arr

solution = Solution()
array = [1,2,3,4,5,6,7,8]
number = 8
print (solution.shuffling(array, number))
