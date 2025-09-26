def solution(my_string):
    answer = ''
    i = len(my_string)
    
    while(i != 0):
        answer += my_string[i-1]
        i -= 1
        
    return answer