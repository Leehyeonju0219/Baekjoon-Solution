from collections import Counter

def solution(s):
    answer = ''
    s = ''.join(sorted(s))
    sH = Counter(s)
    for k,v in sH.items():
        if v == 1:
            answer += k
    return answer