N, K = map(int, input().split())
student = [0] * 13
room = 0

for _ in range(N):
    S, Y = map(int, input().split())
    
    if(S == 0):
        student[(Y * 2) - 1] += 1
    else:
        student[(Y * 2)] += 1

for s in student:
    if s == 0:
        continue
    # 나누어떨어지지 않을 때 자동으로 +1 해주는 식
    room += (s + K - 1) // K

print(room)