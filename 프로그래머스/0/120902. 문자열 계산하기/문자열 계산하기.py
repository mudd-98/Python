def solution(my_string):
    my_s = my_string.split()
    answer = 0
    
    if len(my_s) == 3:
        if my_s[1] == '+':
            answer = int(my_s[0]) + int(my_s[2])
        else:
            answer = int(my_s[0]) - int(my_s[2])
    else:
        if my_s[1] == '+':
            answer = int(my_s[0]) + int(my_s[2])
        else:
            answer = int(my_s[0]) - int(my_s[2])
        
        for i in range(3, len(my_s), 2):
            if my_s[i] == '+':
                answer = answer + int(my_s[i+1])
            else:
                answer = answer - int(my_s[i+1])

    return answer