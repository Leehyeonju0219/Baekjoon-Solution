n = int(input())
for i in range(n):
    tc = input()
    answer = []
    temp = []
    for j in tc:
        if j == '<':
            if answer:
                temp.append(answer.pop())
        elif j == '>':
            if temp:
                answer.append(temp.pop())
        elif j == '-':
            if answer:
                answer.pop()
        else:
            answer.append(j)
    answer.extend(reversed(temp))
    print(''.join(answer))