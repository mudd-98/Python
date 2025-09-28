def solution(arr, divisor):
    tmp = []
    for a in arr:
        if a % divisor == 0:
            tmp.append(a)
            
    if len(tmp) == 0:
        tmp = [-1]
    else:
        tmp.sort()
        
    return tmp