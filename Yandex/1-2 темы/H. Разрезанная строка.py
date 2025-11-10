"""'''
12 3
cabacaqwerty
erty
caba
caqw
'''

n, m = map(int, input().split())

total_string = input()

len_total_string = len(total_string)
len_split_string = len_total_string // m

all_strings = [input().strip() for _ in range(m)]

numbers = []

for i in all_strings:
    pos = total_string.find(i)
    numbers.append(pos)

order = sorted(range(1, len(numbers) + 1), key=lambda i: numbers[i - 1])
print(numbers)
print(*order)
"""

# Вот правильная версия, так как то что сверху решает только до 13 теста

from collections import deque
import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    n, m = map(int, data[0].split())
    s = data[1].strip()
    pieces = [line.strip() for line in data[2:2+m]]

    k = n // m  # длина каждого куска (целочисленное деление)

    # Построим для каждого возможного кусочка в s очередь стартовых позиций
    pos_map = {}
    for i in range(0, n, k):
        sub = s[i:i+k]
        pos_map.setdefault(sub, deque()).append(i)

    # Для каждого входного куска заберём одну доступную позицию (в порядке появления в s)
    assigned = []  # список пар (position, piece_index)
    for idx, piece in enumerate(pieces, start=1):
        if piece not in pos_map or not pos_map[piece]:
            # На всякий случай: но по условию это не должно происходить
            print("ERROR: piece not found", file=sys.stderr)
            pos = -1
        else:
            pos = pos_map[piece].popleft()
        assigned.append((pos, idx))

    # Отсортируем по позиции и выведем индексы кусочков в порядке их следования в s
    assigned.sort(key=lambda x: x[0])
    result = [str(idx) for _, idx in assigned]
    print(" ".join(result))

if __name__ == "__main__":
    main()
