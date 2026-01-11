A, B = map(int, input().split())

# 정수
ans = str(A // B) + "."

# 나머지
remainder = A % B

# 소수점 아래 1000자리
# 10 곱해서 나눔
# 몫은 ans에, 나머지는 다시 10 곱해서 반복
for _ in range(1000):
    remainder *= 10
    ans += str(remainder // B)
    remainder %= B

print(ans)
