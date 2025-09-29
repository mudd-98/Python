def solution(arr, n):
    answer = []
    
    for i, a in enumerate(arr):
        if len(arr) % 2 != 0:
            if i % 2 == 0:
                answer.append(a + n)
            else:
                answer.append(a)
        else:
            if i % 2 != 0:
                answer.append(a + n)
            else:
                answer.append(a)
                
    return answer