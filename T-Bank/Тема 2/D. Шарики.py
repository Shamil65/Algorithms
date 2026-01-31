n = int(input().strip())
colors = list(map(int, input().split()))

def remove_balls(arr):
    total = 0
    while True:
        i = 0 
        n = len(arr)
        while i < n:
            j = i
            while j < n and arr[i] == arr[j]:
                j += 1
            length = j - i
            if length >= 3:
                found = True
                total += length
                arr = arr[:i] + arr[j:]
            i = j
        if not found:
            break
        return total




print(remove_balls(colors))