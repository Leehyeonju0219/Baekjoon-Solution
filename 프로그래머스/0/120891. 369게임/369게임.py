def solution(order):
    answer = 0
    nums = list(map(int, str(order)))
    for num in nums:
        if num == 3 or num == 6 or num == 9:
            answer += 1
    return answer