n, k = map(int, input().split())
a = list(map(int, input().split()))

unique_seen = set()
result = []

# Крок 1: собрать уникальные темы по порядку появления
for x in a:
    if x not in unique_seen:
        unique_seen.add(x)
        result.append(x)
        if len(result) == k:
            break

# Крок 2: дополняем повторяющимися темами до k
if len(result) < k:
    for x in a:
        if x in unique_seen:
            result.append(x)
            if len(result) == k:
                break

print(*result[:k])
