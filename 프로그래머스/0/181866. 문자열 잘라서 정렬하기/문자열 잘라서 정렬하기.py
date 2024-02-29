def solution(myString):
    answer = myString.split("x")
    answer = [value for value in answer if value != '']
    return sorted(answer)