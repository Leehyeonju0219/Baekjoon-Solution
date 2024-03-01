def solution(num, k):
    num_list = list(map(int, str(num)))
    if k not in num_list:
        return -1
    else:
        return num_list.index(k) + 1