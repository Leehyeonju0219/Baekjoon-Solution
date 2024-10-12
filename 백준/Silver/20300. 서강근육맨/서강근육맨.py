machine_num = int(input())
loss = list(map(int, input().split()))
loss.sort()
size = len(loss)

if len(loss) % 2 == 0:
    small = loss[:(size//2)]
    big = list(reversed(loss[(size//2):size]))
else:
    small = loss[:(size//2)]
    big = list(reversed(loss[(size//2):size-1]))

maximum = 0
for i in range(len(small)):
    maximum = max(maximum, small[i] + big[i])

print(max(loss[-1], maximum))