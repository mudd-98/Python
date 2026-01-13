scores = list(map(int, input().split()))
s_max = [100, 100, 200, 200, 300, 300, 400, 400, 500]

if(sum(scores) < 100):
  print("none")
else:
  for i in range(9):
    if(scores[i] > s_max[i]):
      print("hacker")
      break
  else:
    print("draw")