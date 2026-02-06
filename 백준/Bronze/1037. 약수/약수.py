import sys
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

if n % 2 == 0:
  print(nums[0] * nums[-1])
else:
  print(nums[n // 2] ** 2)