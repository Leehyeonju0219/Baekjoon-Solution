def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            temp = board[i][move-1]
            if temp == 0:
                continue
            else:
                board[i][move-1] = 0
                if len(bucket) == 0:
                    bucket.append(temp)
                else:
                    if bucket[-1] == temp:
                        bucket.pop()
                        answer += 2
                    else:
                        bucket.append(temp)
                break

    return answer