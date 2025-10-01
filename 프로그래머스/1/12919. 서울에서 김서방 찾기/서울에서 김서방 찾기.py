def solution(seoul):
    answer = ''
    for i, n in enumerate(seoul):
        if n == 'Kim':
            answer = f'김서방은 {i}에 있다'
            break
    return answer