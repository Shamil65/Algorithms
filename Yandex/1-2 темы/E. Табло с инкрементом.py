n, k = map(int, input().split())

for _ in range(k):
    last_number = n % 10  # более быстрый способ
    n += last_number

print(n)