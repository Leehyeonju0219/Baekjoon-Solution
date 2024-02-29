def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for num in num_list:
        if num % 2 == 0:
            even = int(str(even) + str(num))
        else:
            odd = int(str(odd) + str(num))
            
    answer = odd + even
    return answer