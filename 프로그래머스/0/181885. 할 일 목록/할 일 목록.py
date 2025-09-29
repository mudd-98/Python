def solution(todo_list, finished):
    answer = []
    i = 0
    
    while(i < len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])
        i += 1
        
    return answer