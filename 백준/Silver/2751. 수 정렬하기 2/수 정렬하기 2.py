import sys

n = int(input())
a=[]
for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
for i in range(n):
    print(a[i])