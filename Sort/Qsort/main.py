import random

def quick_sort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr)-1)]
        low = [u for u in arr if u < x]
        eq = [u for u in arr if u == x]
        hi = [u for u in arr if u > x]
        arr = quick_sort(low) + eq + quick_sort(hi)

    return arr

arr = list(range(10, -1, -1))
print(arr)

print("quick_sort: ", quick_sort(arr))