def solution(arr, idx):
    answer = -1
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            if answer != -1:
                break
            else:
                answer = i

    return answer