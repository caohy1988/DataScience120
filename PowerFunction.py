class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0
        elif n == 0:
            return 1
        number = 1
        while n :
            if n & 1:
                number = number * x % d
            n >>= 1
            x = x * x % d
        return number
