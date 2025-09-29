def solution(myString):
    answer = []
    spl_str = myString.split('x')
    for s in spl_str:
        answer.append(len(s))
        
    return answer