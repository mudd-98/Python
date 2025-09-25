def solution(s1, s2):
    answer = 0
    
    s = [x for x in s1 if x in s2]
    answer = len(s)
    
    return answer