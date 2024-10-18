string = input()
string = string.replace('<', '!<')
string = string.replace('>', '>!')
tokens = string.split('!')
tokens = [v for v in tokens if v]
non_flip = {}
flip_tokens = {}

idx = 0
for token in tokens:
    if '<' not in token:
        temp = token.split()
        for j in range(len(temp)):
            flip_tokens[idx] = temp[j]
            idx += 1
    else:
        non_flip[idx] = token
        idx += 1

answer = []
for i in range(len(non_flip) + len(flip_tokens)):
    if i in flip_tokens:
        answer.append(flip_tokens[i][::-1])
        answer.append(' ')
    else:
        if answer and answer[-1] == ' ':
            answer.pop()
        answer.append(non_flip[i])

print(''.join(answer))