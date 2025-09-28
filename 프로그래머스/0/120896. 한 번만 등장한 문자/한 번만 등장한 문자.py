def solution(s):
    tmp = [0] * 26
    answer = ''
    
    for c in s:
        tmp[ord(c) - 97] += 1
    
    for char, n in enumerate(tmp):
        if n == 1:
            answer += chr(char + ord('a'))
    
    s_answer = ''.join(sorted(answer))
    
    return s_answer