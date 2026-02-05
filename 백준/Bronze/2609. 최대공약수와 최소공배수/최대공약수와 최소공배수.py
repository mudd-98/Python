import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())

g = math.gcd(a, b)

l = 0 if a == 0 or b == 0 else a // g * b

print(g)
print(l)