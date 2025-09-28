def solution(order):
    ame = ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]
    latte = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    
    answer = 0
    
    for o in order:
        if o in ame:
            answer += 4500
        else:
            answer += 5000
    
    return answer