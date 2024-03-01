def solution(num_str):
    answer = 0
    num_list = list(map(int, num_str))
    for num in num_list:
        answer += num
    return answer