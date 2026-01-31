import sys
input = sys.stdin.readline

n = int(input())
s = [input().rstrip() for _ in range(n)]
player = [0] * 26
ans = ""

for c in s:
  player[ord(c[0]) - ord('a')] += 1

ans = "".join(chr(i + ord('a')) for i in range(26) if player[i] >= 5)

if ans == "":
  print("PREDAJA")
else:
  print(ans)