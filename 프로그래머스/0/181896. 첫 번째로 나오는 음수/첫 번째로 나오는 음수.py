def solution(num_list):
    answer = 0
    
    for n in num_list:
        if n >= 0:
            answer += 1
        else:
            break
    
    if answer == len(num_list):
        answer = -1
            
    return answer