def solution(a, b):
    result1 = 2*a*b
    result2 = int(str(a) + str(b))
    if result2 >= result1:
        return result2
    return result1