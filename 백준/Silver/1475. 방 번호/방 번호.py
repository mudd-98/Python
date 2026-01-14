N = input()
num_list = [0] * 10

for n in N:
  num_list[int(n)] += 1

# 6과 9는 같은 숫자로 취급
num_list[6] = (num_list[6] + num_list[9] + 1) // 2 
num_list[9] = 0

print(max(num_list))