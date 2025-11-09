from collections import Counter

n, k = map(int, input().split())

my_lists = []

for _ in range(n):
    my_lists.append(list(map(int, input().split())))

# === По горизонтали ===
for my_arr in my_lists:
    O_count = my_arr.count(1)
    X_count = my_arr.count(2)
    if X_count >= 5 or O_count >= 5:
        print("Yes")
        break

# === По вертикали ===
# k - это наша ширина
X_count = 0
O_count = 0
for i in range(k):
    for my_arr in my_lists:
        if my_arr[i] == 1:
            X_count += 1
        else:    
            O_count += 1
        if X_count >= 5 or O_count >= 5:
            print("yes")
            break
    X_count = 0
    O_count = 0




print(my_lists)