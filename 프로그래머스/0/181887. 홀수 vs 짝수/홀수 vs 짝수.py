def solution(num_list):
    answer = 0
    odd_sum = sum(num_list[0 : : 2])
    even_sum = sum(num_list[1 : : 2])
    
    if odd_sum > even_sum:
        answer = odd_sum
    elif odd_sum < even_sum:
        answer = even_sum
    else:
        answer = even_sum
    
    return answer