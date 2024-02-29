def solution(myString):
    answer = []
    str_list = myString.split('x')
    for string in str_list:
        answer.append(len(string))
    return answer