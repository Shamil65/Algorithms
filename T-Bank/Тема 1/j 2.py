# # t = int(input())

# # list_arr = []
# # for _ in range(t):
# #     a = list(map(int, input().split()))
# #     list_arr.append(a)

# def L_R(k):
#     L = (((n-1)*m*n + (k+1)*n)*k)/2
#     R = (((n-1)*m*n + (k+1+m)*n)*(m-k))/2
#     return L, R

# def U_D(k):
#     U = ((k*(m**2) + m)*k)/2
#     D = (((k+n)*m**2 + m)*(n-k))/2
#     return U, D

# # for ar in list_arr:

# #     # Строки пронумерованы от 1 до n, столбцы пронумерованы от 1 до m
# #     n, m = ar[0], ar[1]


# #     min_ver_border=0
# #     # Если столбоц всего 1 шт то ответа нет
# #     # Нахождение границы для столбцов
# #     for k in range( m+1):
# #         if m <= 1:
# #             abs_ver_dif = float('inf')
# #             break
# #         # print("k: ", k+1)
        
# #         L, R = L_R(k)
# #         print("k: ", k+1, "|","L: ", L, "|", " R: ", R, "|", abs(L-R))

# #         # max(k): L < = R
# #         if L > R:
# #             L_, R_ = L_R(k-1)
# #             if abs(L-R) < abs(L_ - R_):
# #                 min_ver_border, abs_ver_dif = k+1, abs(L-R)
# #             else:
# #                 min_ver_border, abs_ver_dif = k, abs(L_ - R_)
# #             break
# #         else:
# #             k += 1



# #     min_hor_border = 0
# #     # Нахождение границы для строк
# #     for k in range( n+1):
# #         if n <= 1:
# #             abs_hor_dif = float('inf')
# #             break
# #         # print("k: ", k)
        
# #         U, D = U_D(k)
# #         # print("U: ", U, " D: ", D, abs(U-D))

# #         # max(k): U < = D
# #         if U > D:
# #             U_, D_ = U_D(k-1)
# #             if abs(U-D) < abs(U_ - D_):
# #                 min_hor_border, abs_hor_dif = k+1, abs(U-D)
# #             else:
# #                 min_hor_border, abs_hor_dif = k, abs(U_ - D_)
# #             break
# #         else:
# #             k += 1
# #     # print(min_hor_border, "hor", abs_hor_dif)

# #     if abs_ver_dif > abs_hor_dif:
# #         print(f"H {min_hor_border}")
# #     elif abs_ver_dif == abs_hor_dif:
# #         print(f"V {min_ver_border}")
# #     else:
# #         print(f"V {min_ver_border}")


# # Возможны варианты n = 1 или m = 1

# # соседние k равны а я беру больший

# # Если правильных ответов несколько, то надо вывести вариант с вертикальным разрезом, если
# # он есть, а если и после этого вариантов несколько, то из вариантов с различными x следует выбрать
# # тот, в котором x меньше


# # Строки пронумерованы от 1 до n, столбцы пронумерованы от 1 до m


# # left_LR = 0
# # right_LR = m


# # # for ar in list_arr:

# # # Строки пронумерованы от 1 до n, столбцы пронумерованы от 1 до m
# n, m = 2, 4
# min_ver_border=0
# k = 0
# # расчет для столбцов L и R

# left = 0
# right = m


# while left != right:

#     mid = (left + right) // 2

#     print(mid)
#     L, R = L_R(mid)
#     L_plus_1, R_plus_1 = L_R(mid+1)
#     L_minus_1, R_minus_1= L_R(mid-1)

#     if 

#     if abs(L-R) > abs(L_plus_1 - R_plus_1):
#         left = mid + 1
#         # right также
#     elif abs(L-R) > abs(L_minus_1 - R_minus_1):
#         right = mid - 1
#         # left  также


def L_R(k):
    L = (((n-1)*m*n + (k+1)*n)*k)/2
    R = (((n-1)*m*n + (k+1+m)*n)*(m-k))/2
    return L, R

def U_D(k):
    U = ((k*(m**2) + m)*k)/2
    D = (((k+n)*m**2 + m)*(n-k))/2
    return U, D


def find_vertical(n, m):
    if m <= 1:
        return float('inf'), 1

    def f(k):
        L, R = L_R(k)
        return L - R

    left, right = 0, m
    while left < right:
        mid = (left + right) // 2
        if f(mid) >= 0:
            right = mid
        else:
            left = mid + 1

    best = []
    for k in (left-1, left):
        if 0 <= k <= m:
            L, R = L_R(k)
            best.append((abs(L-R), k))

    best.sort()
    diff, k = best[0]
    return diff, k+1


def find_horizontal(n, m):
    if n <= 1:
        return float('inf'), 1

    def f(k):
        U, D = U_D(k)
        return U - D

    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if f(mid) >= 0:
            right = mid
        else:
            left = mid + 1

    best = []
    for k in (left-1, left):
        if 0 <= k <= n:
            U, D = U_D(k)
            best.append((abs(U-D), k))

    best.sort()
    diff, k = best[0]
    return diff, k+1






t = int(input())

list_arr = []
for _ in range(t):
    a = list(map(int, input().split()))
    list_arr.append(a)


for ar in list_arr:

    # Строки пронумерованы от 1 до n, столбцы пронумерованы от 1 до m
    n, m = ar[0], ar[1]

    abs_ver_dif, min_ver_border = find_vertical(n, m)
    abs_hor_dif, min_hor_border = find_horizontal(n, m)

    if abs_ver_dif <= abs_hor_dif:
        print("V", min_ver_border)
    else:
        print("H", min_hor_border)