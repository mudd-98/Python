def solution(my_string, indices):
    lst_str = list(my_string)
    
    for i in indices:
        lst_str[i] = ''
    
    answer = ''.join(lst_str)
    
    return answer