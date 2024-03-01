def solution(n):
    answer = [[0] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    _dir = 0
    x, y = 0, 0
    answer[0][0] = 1
    for i in range(1, n * n):
        if x + dx[_dir] >= n or x + dx[_dir] <= -1 or y + dy[_dir] >= n or y + dy[_dir] <= -1 or answer[y+dy[_dir]][x+dx[_dir]] != 0:
            _dir = (_dir+1)%4
        answer[y + dy[_dir]][x + dx[_dir]] = i + 1
        y += dy[_dir]
        x += dx[_dir]

    return answer
        
    return answer