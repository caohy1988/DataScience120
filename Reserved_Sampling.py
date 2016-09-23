# Reserved Sampling
# Author: Haiyuan Cao
# Given a stream of n samples, and take a random sample of k elements.
# 1. Create an array reservoir[0..k-1] and copy first k items of stream[] to it.
# 2. Now one by one consider all items from (k+1)th item to nth item.
# 3. Generate a random number from 0 to i where i is index of current item in stream[]. Let the generated random number is j.
# 4. If j is in range 0 to k-1, replace reservoir[j] with stream[i]
import random
class Solution(object):
    def reserved_sampling(self, stream_input, k):
        n = len(stream_input)
        reserver = []
        for i in range(0, k):
            reserver.append(stream_input[i])
        i = k
        while i < n:
            index = random.randint(0, i)
            if index < k:
                reserver[index] = stream[i]
            i += 1

        return reserver

stream = [1,2,3,5,6,7,8,9,10]
k = 3
solution = Solution()
print (solution.reserved_sampling(stream, k))
