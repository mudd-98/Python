import sys
import math
input = sys.stdin.readline

n = int(input())

if n == 0:
  print(1)
else:
  print(math.factorial(n))