from collections import Counter

s = input().strip()
n = len(s)
cnt = Counter(s)

total_pairs = n*(n-1)//2
same_pairs = sum(v*(v-1)//2 for v in cnt.values())

answer = 1 + total_pairs - same_pairs
print(answer)
