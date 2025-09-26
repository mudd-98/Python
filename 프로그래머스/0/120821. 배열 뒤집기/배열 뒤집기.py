def solution(num_list):
    answer = []
    i = len(num_list)
    
    while(i != 0):
        answer.append(num_list[i-1])
        i -= 1
    
    return answer