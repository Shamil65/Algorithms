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



arr = list(range(10))
print(arr)

left = 0
right = len(arr)-1
        

def anti_qsort(arr):
    if len(arr) > 1:
        x = arr[(left + right) // 2]