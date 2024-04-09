from sys import stdin

num = int(stdin.readline())

same = {}
answer = 0
for i in range(num):
    A, B = stdin.readline().split()
    A = A[:2]

    if A == B:
        continue

    if same.get((A,B)) == None:
        same[(A,B)] = 0
    same[(A,B)] += 1

    if same.get((B,A)) != None:
        answer += same[(B,A)]

print(answer)