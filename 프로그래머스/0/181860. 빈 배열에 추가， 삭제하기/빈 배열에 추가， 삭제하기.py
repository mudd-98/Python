def solution(arr, flag):
    X = []
    i = 0
    
    for f in flag:
        if f == True:
            m = arr[i] * 2
            while(m != 0):
                X.append(arr[i])
                m -= 1
        else:
            n = arr[i]
            if len(X) > 0:
                while(n != 0):
                    X.pop()
                    n -= 1
        i += 1
    return X