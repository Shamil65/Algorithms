n, k = map(int, input().split())

while k > 0:
    x = n % 10
    if x == 0:
        break
    if x == 2:
        n += (k // 4) * 20
        k %= 4
        if k == 0:
            break
    n += x
    k -= 1

print(n)
