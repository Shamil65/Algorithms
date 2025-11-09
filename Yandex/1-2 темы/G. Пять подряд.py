import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("No")
        return

    # Парсим первую строку с n и m — с защитой от ошибок формата
    first_parts = data[0].strip().split()
    if len(first_parts) < 2:
        print("No")
        return
    try:
        n = int(first_parts[0])
        m = int(first_parts[1])
    except:
        print("No")
        return

    # Считываем поле — если строк меньше, дополним точками
    field = []
    for i in range(n):
        if i + 1 < len(data):
            row = data[i+1].rstrip('\n')
        else:
            row = ""
        # если строка длиннее m, обрезаем; если короче — дополняем точками
        if len(row) < m:
            row = row.ljust(m, '.')
        elif len(row) > m:
            row = row[:m]
        field.append(row)

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
                    return
    print("No")

if __name__ == "__main__":
    main()
