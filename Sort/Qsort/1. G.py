n = int(input())

arr = list(range(1, n+1)) # n=10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def anti_quik_sort(n):
    qarr = [0] * n
    pos = 0
    nums = list(range(1, n + 1))

    def block(l, r):
        nonlocal pos
        if l > r:
            return
        m = (l + r) // 2
        qarr[m] = nums[pos]
        pos += 1
        block(l, m-1)
        block(m+1, r)
        
    block(0, n-1)
    return qarr

print(*anti_quik_sort(n))