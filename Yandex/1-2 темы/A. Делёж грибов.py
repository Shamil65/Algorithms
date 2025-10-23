n = int(input())
arr = list(map(int, input().split()))

even_nbs = [arr[i] for i in range(0, len(arr), 2)]
odd_nbs = [arr[i] for i in range(1, len(arr), 2)]

# print(even_nbs, odd_nbs)

sum_Vasya = sum(even_nbs)
sum_Masha = sum(odd_nbs)

R_init = sum_Vasya - sum_Masha

min_Vasya = min(even_nbs)
max_Masha = max(odd_nbs)

if max_Masha > min_Vasya:
    index_min_Vasya = even_nbs.index(min_Vasya)
    index_max_Masha = odd_nbs.index(max_Masha)

    even_nbs[index_min_Vasya], odd_nbs[index_max_Masha] = odd_nbs[index_max_Masha], even_nbs[index_min_Vasya]

print(sum(even_nbs) - sum(odd_nbs))