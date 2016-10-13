def count_item(n):
    return (1 + (n-2)) * (n-2) / 2
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = 1
        length = len(A)
        set_diff = set()
        count_total = 0
        if length < 3:
            return 0
        else:
            while index < length:
                difference = A[index] - A[index-1]
                print difference
                if len(set_diff) == 0:
                    set_diff.add(difference)
                    count = 1
                else:
                    if difference in set_diff:
                        count += 1
                    else:
                        count_total += count_item(count+1)
                        print count_total
                        set_diff = set()
                        count = 1
                        set_diff.add(difference)
                index += 1
        print (count)
        count_total += count_item(count+1)
        return count_total
