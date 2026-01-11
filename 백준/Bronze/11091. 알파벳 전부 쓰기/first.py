N = int(input())

for i in range(N):
  alp = [0] * 26
  ans = ""
  
  s = input()
  s = s.lower()
  
  for c in s:
    if c.isalpha():
      alp[ord(c) - ord('a')] = 1

  if sum(alp) == 26:
    print("pangram")
  else:
    for i in range(26):
      if alp[i] == 0:
        ans += chr(ord('a') + i)
        
    print(f'missing {ans}')
