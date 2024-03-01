def solution(n):
    answer = 0
    num_list = list(map(int,str(n)))
    for num in num_list:
        answer += num
    return answer