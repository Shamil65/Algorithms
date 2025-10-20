arr = list(range(10))
print(arr)

hidden_number = int(input("Введите число: "))
left = 0
right = len(arr) - 1

while left != right:
    mid = (left + right) // 2

    if mid == hidden_number:
        print(mid)
    elif mid > hidden_number:
        right = mid - 1
    else:
        left = mid + 1