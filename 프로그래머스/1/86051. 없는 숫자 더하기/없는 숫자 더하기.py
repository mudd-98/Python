def solution(numbers):
    tmp = [0] * 10
    answer = 0
    
    for n in numbers:
        tmp[n] += 1
    
    for i, cnt in enumerate(tmp):
        if cnt == 0:
            answer += i
    
    return answer