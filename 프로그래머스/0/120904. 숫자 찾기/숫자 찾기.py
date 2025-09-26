def solution(num, k):
    answer = -1
    numlist = list(str(num))
    
    for i in numlist:
        if i == str(k):
            answer = numlist.index(i) + 1
            break
    
    return answer