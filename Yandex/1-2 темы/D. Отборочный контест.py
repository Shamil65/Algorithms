n, k = map(int, input().split())
themes = list(map(int, input().split()))

# Считаем количество задач по каждой теме
from collections import Counter
count = Counter(themes)

# Сначала выбираем по одной задаче из каждой темы
selected = []
for theme in count:
    selected.append(theme)
    
    count[theme] -= 1
    print("count[theme]: ", count[theme], "theme ", theme, "count ", count)
    if len(selected) == k:
        break

# Если ещё не набрали k задач, добавляем оставшиеся из тех, где больше одной задачи
if len(selected) < k:
    for theme in count:
        while count[theme] > 0 and len(selected) < k:
            selected.append(theme)
            count[theme] -= 1

print(*selected)
