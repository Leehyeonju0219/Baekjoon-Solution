def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
    
    start_idx = arr.index(2)
    end_idx = len(arr) - arr[::-1].index(2)
    
    answer = arr[start_idx:end_idx]
    
    return answer