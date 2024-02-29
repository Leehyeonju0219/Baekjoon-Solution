def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if pat in myString:
            answer += 1
            idx = myString.index(pat)
            myString = myString[idx+1:]
    return answer