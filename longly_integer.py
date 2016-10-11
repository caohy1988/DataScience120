import sys

from functools import reduce
from operator import xor

input()
print(reduce(xor, map(int, input().split())))
