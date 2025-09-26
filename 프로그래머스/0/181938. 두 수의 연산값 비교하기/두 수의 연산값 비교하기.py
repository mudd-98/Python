def solution(a, b):
    answer = 0
    
    ab_plus = int(f"{a}{b}")
    ab_mul = 2 * a * b
    
    if (ab_plus == ab_mul):
        answer = ab_plus
    else:
        answer = max(ab_plus, ab_mul)
    
    return answer