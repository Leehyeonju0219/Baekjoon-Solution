from sys import stdin

n = int(stdin.readline())
liqs = list(map(int, stdin.readline().split(" ")))
liqs.sort()

left = 0
right = n-1
min = abs(liqs[left] + liqs[right])
result = [liqs[left], liqs[right]]

while left < right:
    sum = liqs[left] + liqs[right]
    if abs(sum) < min:
        result = [liqs[left], liqs[right]]
        min = abs(sum)

    if min == 0:
        break

    if sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])