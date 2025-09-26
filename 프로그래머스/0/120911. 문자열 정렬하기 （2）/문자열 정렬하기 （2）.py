def solution(my_string):
    answer = ''
    
    low_str = my_string.lower()
    s_answer = sorted(low_str)
    answer = "".join(s_answer)
    
    return answer