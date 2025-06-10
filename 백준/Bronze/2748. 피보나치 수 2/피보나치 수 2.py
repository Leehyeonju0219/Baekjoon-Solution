n = int(input())

n1 = 0
n2 = result = 1
for i in range(n-1):
    result = n1+n2
    n1 = n2
    n2 = result
    

print(result)