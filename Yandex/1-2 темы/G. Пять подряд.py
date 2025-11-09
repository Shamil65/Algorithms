n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# 4 направления: (dx, dy)
directions = [
    (0, 1),   # вправо
    (1, 0),   # вниз
    (1, 1),   # диагональ вниз-вправо
    (1, -1)   # диагональ вниз-влево
]

for i in range(n):
    for j in range(m):
        if field[i][j] in ('X', 'O'):
            sym = field[i][j]
            for dx, dy in directions:
                count = 1
                x, y = i, j
                for k in range(4):  # нужно ещё 4 клетки (всего 5)
                    x += dx
                    y += dy
                    if 0 <= x < n and 0 <= y < m and field[x][y] == sym:
                        count += 1
                    else:
                        break
                if count == 5:
                    print("Yes")
                    exit()
print("No")
