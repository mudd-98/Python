def solution(absolutes, signs):
    answer = 0
    i = 0
    
    while(i < len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += -(absolutes[i])
        i += 1
    
    return answer