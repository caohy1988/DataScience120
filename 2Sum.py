# 2 Sum
# Author: Haiyuan Cao
# Date: Oct 4, 2016
def two_sum(m, n, array):
    hashtable = {}
    index = 0
    while index < n:
        if array[index] < m:
            if array[index] in hashtable.keys():
                return (hashtable[array[index]]+1, index+1)
            else:
                hashtable [m-array[index]] = index
                index += 1
        else:
            index += 1

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    (index1, index2) = two_sum(m, n, a)
    print (index1, index2)
