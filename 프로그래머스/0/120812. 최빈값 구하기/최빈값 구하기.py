from collections import Counter

def solution(array):
    answer = []
    dH = Counter(array)
    max_value = max(dH.values())
    result = 0
    for key in dH:
        if dH[key] == max_value:
            answer.append(key)
            result = key
            
    if len(answer) > 1:
        result = -1
    return result