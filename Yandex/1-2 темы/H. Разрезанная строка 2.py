n, m = map(int, input().split())

full_string = input()

arr_strings = [ input() for _ in range(m) ]

k = n // m

add = {}
for i in range(0,n,k):
    mini = full_string[i:i+k]
    passs_arr = add.setdefault(mini, [])
    passs_arr.append(i)
    print(i)
    print(mini)
    print(add)
    print(passs_arr)

assigned = []
for indx, value in enumerate(arr_strings, start=1):
    popp = add[value].pop(0)
    assigned.append((popp, indx))

assigned.sort(key=lambda x: x[0])



print(assigned)