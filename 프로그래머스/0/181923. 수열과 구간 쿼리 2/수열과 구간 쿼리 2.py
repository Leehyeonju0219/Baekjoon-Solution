def solution(arr, queries):
    answer = []
    for query in queries:
        temp = arr[query[0]:query[1]+1]
        min = max(arr)+1
        for num in temp:
            if num > query[2]:
                if num < min:
                    min = num
                    
        if min == max(arr)+1:
            answer.append(-1)
        else:
            answer.append(min)
                
    return answer