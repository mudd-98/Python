def solution(my_strings, parts):
    answer = ''
    
    for i, s in enumerate(my_strings):
        a, b = parts[i]
        answer += s[a:b+1]
    
    return answer