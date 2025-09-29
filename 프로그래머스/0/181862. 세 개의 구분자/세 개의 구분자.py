def solution(myStr):
    
    rep_str = myStr.replace('a', 'c')
    rep_str2 = rep_str.replace('b', 'c')
    answer = rep_str2.split('c')
    
    filtered = list(filter(None, answer))
    
    if len(filtered) == 0:
        filtered = ["EMPTY"]
    
    return filtered