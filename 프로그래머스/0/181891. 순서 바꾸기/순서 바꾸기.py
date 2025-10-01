def solution(num_list, n):
    n_after = num_list[n : ]
    n_bef = num_list[ : n]
    answer = n_after + n_bef
    
    return answer