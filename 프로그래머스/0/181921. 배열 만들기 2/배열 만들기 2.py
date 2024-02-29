def solution(l, r):
    answer = []
    rest_nums = [1,2,3,4,6,7,8,9]
    for i in range(l, r+1):
        nums = list(map(int, str(i)))
        flag = True
        for j in nums:
            if j in rest_nums:
                flag = False
                break
        if flag:
            answer.append(i)
        else:
            continue
            
    if len(answer) == 0:
        answer.append(-1)
    return answer