def solution(my_string):
    answer = my_string.split(" ")
    answer = [value for value in answer if value != '']
    return answer