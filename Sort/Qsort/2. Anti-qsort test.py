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

#---------------------------------------------------------------
#---------------------------------------------------------------

# Основной механизм завершения - условие выхода из рекурсии
# Ключевой момент - это условие в начале функции:

# python
# def qsort(a, left, right):
#     if right < left:  # ⬅️ УСЛОВИЕ ВЫХОДА ИЗ РЕКУРСИИ
#         return

# arr = [3, 6, 1, 8, 4, 5]:

# qsort(0,5)
#     ├── qsort(0,0) → завершается (j = -1)
#     └── qsort(1,5)
#         ├── qsort(1,2) → завершается
#         └── qsort(3,5) → завершается

# Но в конце просто return, это значит что просто ничего не возвращаем, 
# так как мы работаем не с данными котрые надо возвращать, а с массивом, 
# котторый постоянно редактируем

#---------------------------------------------------------------
#---------------------------------------------------------------


# def anti_qsort(n):
#     a = [0] * n
#     nums = list(range(1, n + 1))
#     pos = 0  # текущая позиция в nums

#     def build(l, r):
#         nonlocal pos
#         if l > r:
#             return
#         m = (l + r) // 2
#         a[m] = nums[pos]
#         pos += 1
#         build(l, m - 1)
#         build(m + 1, r)

#     build(0, n - 1)
#     return a

# n = int(input())
# print(*anti_qsort(n))
