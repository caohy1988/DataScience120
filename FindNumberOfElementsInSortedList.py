class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        length = len(A)
        low = 0
        high = length - 1
        f = -1
        while low <= high:
            mid=int((low+high)/2)
            if A[mid]==B:
                f=mid
                high=mid-1
            elif A[mid]>B:
                high=mid-1
            else:
               low=mid+1
        if f==-1:
           return 0
        s=-1
        low=f
        high=length-1
        while low<=high:
            mid=int((low+high)/2)
            if A[mid]==B:
                s=mid
                low=mid+1
            elif A[mid]>B:
                high=mid-1
            else:
                low=mid+1
        return s-f+1
