def main():
    # Чтение входа
    n, m = map(int, input().split())
    s = input().strip()
    pieces = [input().strip() for _ in range(m)]

    k = n // m  # длина каждого куска

    # Создаём словарь: кусок -> список всех позиций в s
    pos_map = {}
    for i in range(0, n, k):
        sub = s[i:i+k]
        ppmi = pos_map.setdefault(sub, [])
        ppmi.append(i)

    assigned = []
    # Для каждого куска из входных данных находим его позицию
    for idx, piece in enumerate(pieces, start=1):
        pos = pos_map[piece].pop(0)  # достаем первую позицию
        assigned.append((pos, idx))
    # Сортируем по позиции в исходной строке
    assigned.sort(key=lambda x: x[0])
    result = [str(idx) for _, idx in assigned]

    print(" ".join(result))

if __name__ == "__main__":
    main()
