def solution(num_list):
    answer = 0
    n_mul = 1
    n_sum = 0
    
    for i in num_list:
        n_mul *= i
        n_sum += i
    
    if n_mul < n_sum ** 2:
        answer = 1
    else :
        answer = 0
    
    return answer