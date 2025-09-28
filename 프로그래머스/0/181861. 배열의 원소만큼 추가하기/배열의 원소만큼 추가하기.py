def solution(arr):
    X = []
    
    for a in arr:
        a_list = [a] * a
        X.extend(a_list)
    
    return X