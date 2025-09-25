def solution(myString):
    answer = ''
    
    for s in myString:
        if s.islower():
            answer += s
        else:
            answer += s.lower()
    
    return answer