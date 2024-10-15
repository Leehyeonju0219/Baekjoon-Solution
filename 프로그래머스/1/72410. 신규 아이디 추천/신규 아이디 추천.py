from collections import deque

def solution(new_id):
    special_char = {'~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', ']', '{', '}', ':', '?', ',', '<', '>', '/'}
    id_char = list(new_id)
    
    # 1단계
    for i in range(len(id_char)):
        if ord(id_char[i]) >= 65 and ord(id_char[i]) <= 90:
            id_char[i] = chr(ord(id_char[i]) + 32)
    
    # 2단계
    id_char = list(filter(lambda x: x not in special_char, id_char))
    
    # 3단계
    is_consecutive = False
    delete_list = []
    for i in range(len(id_char)):
        if id_char[i] == '.':
            if is_consecutive:
                delete_list.append(i)
            else:
                is_consecutive = True
        else:
            is_consecutive = False
    
    delete_list.reverse()
    for i in delete_list:
        id_char.pop(i)
    
    # 4단계
    temp_deque = deque(id_char)
    if id_char:
        if id_char[0] == '.':
            temp_deque.popleft()
        if temp_deque and id_char[len(id_char)-1] == '.':
            temp_deque.pop()
    id_char = list(temp_deque)
    
    # 5단계
    if not id_char:
        id_char.append('a')
        
    # 6단계
    if len(id_char) >= 16:
        id_char = id_char[:15]
        if id_char[14] == '.':
            id_char.pop()
            
    # 7단계
    if len(id_char) <= 2:
        while len(id_char) < 3:
            id_char.append(id_char[len(id_char)-1])
    
    return ''.join(id_char)