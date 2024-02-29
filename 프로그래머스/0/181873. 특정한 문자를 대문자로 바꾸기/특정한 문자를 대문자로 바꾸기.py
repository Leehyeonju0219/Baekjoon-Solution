def solution(my_string, alp):
    answer = ''
    str_list = list(my_string)
    for i in range(len(str_list)):
        if str_list[i] == alp:
            str_list[i] = str_list[i].upper()
    return ''.join(str_list)