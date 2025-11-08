n, k = map(int, input().split())

for i in range(k):
    n_str = str(n)
    last_number = int(n_str[-1])

    n += last_number

print(n)