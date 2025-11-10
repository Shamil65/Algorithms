n, m = map(int, input().split())

field = [input().strip() for _ in range(n)]

# направления: вправо, вниз, диагональ вниз-вправо, диагональ вниз-влево
directions = [(0,1),(1,0),(1,1),(1,-1)]
for i in range(n):
    for j in range(m):
        ch = field[i][j]
        if ch not in ('X','O'):
            continue
        for dx, dy in directions:
            x, y = i, j
            cnt = 1
            for _ in range(4):  # ещё 4 шагa для общей длины 5
                x += dx
                y += dy
                if 0 <= x < n and 0 <= y < m and field[x][y] == ch:
                    cnt += 1
                else:
                    break
            if cnt == 5:
                print("Yes")

