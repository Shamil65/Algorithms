k = int(input())
arr_L = list(map(int, input().split()))

# arr_L.append(arr_L[0])

arr_zero = [0]*k


ans = []
for j in arr_L:

    m=0

    l1 = list(arr_zero)
    for iteration in range(k):
        had_swaps = False
        for i in range(k - 1):
            if l1[i] > l1[i + 1]:
                l1[i], l1[i + 1] = l1[i + 1], l1[i]
                had_swaps = True
        m += 1
        if not had_swaps:
            break
    arr_zero[j-1] = 1
    ans.append(m)
    
    
print(*ans)

    
