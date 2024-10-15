def solution(s):
    answer = 1001
    s_size = len(s)
    for i in range(s_size):
        min_length = 0
        ch = s[:i+1]
        length = 0
        for j in range(0, s_size, i+1):
            if ch == s[j:j+i+1]:
                length += 1
            else:
                if length == 1:
                    min_length += len(ch)
                else:
                    min_length += len(ch) + len(str(length))
                ch = s[j:j+i+1]
                length = 1
        
        if length == 1:
            min_length += len(ch)
        else:
            min_length += len(ch) + len(str(length))
            
        answer = min(answer, min_length)
        
    return answer