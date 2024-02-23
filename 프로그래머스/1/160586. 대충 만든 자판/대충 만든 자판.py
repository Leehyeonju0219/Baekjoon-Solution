from collections import defaultdict

def solution(keymap, targets):
    answer = []
    dH = defaultdict(int)
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if dH[keymap[i][j]] == 0 or dH[keymap[i][j]] > j+1:
                dH[keymap[i][j]] = j + 1
    
    for target in targets:
        cnt = 0
        flag = False
        for ch in target:
            if ch in dH:
                cnt += dH[ch]
            else:
                flag = True
                break
        if flag:
            answer.append(-1)
        else:
            answer.append(cnt)
        
    return answer