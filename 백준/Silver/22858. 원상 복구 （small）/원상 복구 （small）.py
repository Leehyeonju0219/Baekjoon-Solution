num_of_card, num_of_shuffle = map(int, input().split())
shuffle_result = list(map(int, input().split()))
d = list(map(int, input().split()))

p = [0] * num_of_card
for _ in range(num_of_shuffle):
    for i in range(num_of_card):
        p[d[i]-1] = shuffle_result[i]
    shuffle_result = p.copy()

print(' '.join(map(str,p)))