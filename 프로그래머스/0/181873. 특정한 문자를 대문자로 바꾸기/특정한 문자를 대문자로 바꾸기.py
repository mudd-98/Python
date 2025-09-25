def solution(my_string, alp):
    answer = ''
    
    for s in my_string:
        if (s != alp):
            answer += s
            continue
        else:
            answer += s.upper()
            
    return answer