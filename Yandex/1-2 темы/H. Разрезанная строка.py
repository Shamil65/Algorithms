'''
12 3
cabacaqwerty
erty
caba
caqw
'''

n, m = map(int, input().split())

total_string = input()

len_total_string = len(total_string)
len_split_string = len_total_string/m

all_strings = [input().strip() for _ in range(m)]


print(all_strings)