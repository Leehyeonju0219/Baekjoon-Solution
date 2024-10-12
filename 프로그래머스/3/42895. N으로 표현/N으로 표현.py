from itertools import product

def solution(N, number):
    dp = [set() for _ in range(9)]

    if N == number:
        return 1
    else:
        dp[1].add(N)

    for i in range(2,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            for x,y in product(dp[j],dp[i-j]):
                dp[i].update({x+y,x-y,x*y})
                if y != 0:
                    dp[i].add(x//y)
        if number in dp[i]:
            return i
    return -1