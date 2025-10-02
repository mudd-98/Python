def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    
    srt_ans = sorted(answer)
    return srt_ans