# def qsort(a, left, right):
#     # Сортировка a[left...right] включительно
#     if right < left:
#         return

#     q = a[(left + right) // 2]
#     i = left
#     j = right

#     while i <= j:
#         while a[i] < q:
#             i += 1
#         while a[j] > q:
#             j -= 1
#         if i <= j:
#             a[i], a[j] = a[j], a[i]  # swap
#             i += 1
#             j -= 1

#     qsort(a, left, j)
#     qsort(a, i, right)


# # Пример использования:
# arr = [3, 6, 1, 8, 4, 5]
# qsort(arr, 0, len(arr)-1)
# print(arr)  # [1, 3, 4, 5, 6, 8]



arr = list(range(1, 8))
print(arr)

left = 0
right = len(arr)-1

ind_av_pos = (left + right) // 2

x = arr[(left + right) // 2]
print("Число ->", x, "Его индекс ->", ind_av_pos)

arr[ind_av_pos] = arr[-1]

print("Новый массив", arr)


      

def anti_qsort(n):
    a = [0] * n
    nums = list(range(1, n + 1))
    pos = 0  # текущая позиция в nums

    def build(l, r):
        nonlocal pos
        if l > r:
            return
        m = (l + r) // 2
        a[m] = nums[pos]
        pos += 1
        build(l, m - 1)
        build(m + 1, r)

    build(0, n - 1)
    return a

n = int(input())
print(*anti_qsort(n))
