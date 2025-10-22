def anti_quicksort(n):
    a = list(range(1, n + 1))
    for i in range(2, n):
        a[i], a[i // 2] = a[i // 2], a[i]
        print("a[i]: ", a[i], " --- ", "a[i // 2]: ", a[i // 2])
        print("a: ", a)
    return a

n = int(input())
print(*anti_quicksort(n))