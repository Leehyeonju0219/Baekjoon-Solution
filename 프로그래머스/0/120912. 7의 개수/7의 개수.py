def solution(array):
    answer = 0
    for num in array:
        num_list = list(map(int, str(num)))
        for i in range(len(num_list)):
            if num_list[i] == 7:
                answer += 1
    return answer