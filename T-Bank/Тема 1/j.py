# t = int(input())

# list_arr = []
# for _ in range(t):
#     a = list(map(int, input().split()))
#     list_arr.append(a)

# # print(list_arr)

# def L_R(k):
#     L = (((n-1)*m*n + (k+1)*n)*k)/2
#     R = (((n-1)*m*n + (k+1+m)*n)*(m-k))/2
#     return L, R

# def U_D(k):
#     U = ((k*(m**2) + m)*k)/2
#     D = (((k+n)*m**2 + m)*(n-k))/2
#     return U, D


# # ======================================

# for i in list_arr:
#     n, m = i[0], i[1]
#     # print(n, m)

#     # max(k): L < = R
#     L = 0
#     R = 0
#     for k in range(m):
        
#         if L > R:
#             break
#         else:
#             L, R = L_R(k)
#             k+=1

#     L_, R_ = L_R(k-1)   
#     if abs(L-R) > abs(L_-R_):
#         k = k - 1
#         # print("V", k, " abs(L_-R_) ", abs(L_-R_))
#         sum_v, v = abs(L_-R_), k

#     else:
#         # print("V", k, " abs(L-R) ", abs(L-R))
#         sum_v, v = abs(L-R), k
        
#     # =================

#     U = 0
#     D = 0
#     for j in range(m):
        
#         if U > D:
#             break
#         else:
#             U, D = U_D(j)
#             j+=1

#     U_, D_ = U_D(j-1)   
#     if abs(U-D) > abs(U_-D_):
#         j = j-1
#         # print("H", j, " abs(U-D) ", abs(U_-D_))
#         sum_h, h = abs(U_-D_), j
#     else:
#         # print("H", j, " abs(U-D) ", abs(U-D))
#         sum_h, h = abs(U-D), j
#         h = j

#     h_ans = f"H{h}"
#     v_ans = f"V{v}" 


#     if sum_h < sum_v:
#         print(h_ans)
#     elif sum_h == sum_v:
#         print(v_ans)
#     else:
#         print(v_ans)




import sys
input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    total = n * m * (n * m + 1) // 2

    # Вертикаль
    v_diff = float('inf')
    v_k = 0
    sum_left = 0
    cells_left = 0
    for k in range(1, m):
        cells_left += n
        sum_left += cells_left
        diff = abs(2 * sum_left - total)
        if diff < v_diff:
            v_diff, v_k = diff, k

    # Горизонталь
    h_diff = float('inf')
    h_k = 0
    sum_top = 0
    cells_top = 0
    for k in range(1, n):
        cells_top += m
        sum_top += cells_top
        diff = abs(2 * sum_top - total)
        if diff < h_diff:
            h_diff, h_k = diff, k

    if h_diff < v_diff or (h_diff == v_diff and "H" < "V"):  # или другое правило при равенстве
        print(f"H{h_k}")
    else:
        print(f"V{v_k}")