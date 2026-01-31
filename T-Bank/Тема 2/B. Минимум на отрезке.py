# import sys
# from collections import deque

# data = sys.stdin.read().split()

# arr = list(map(int, data))

# deque_arr = deque(arr)
# N = deque_arr.popleft()
# K = deque_arr.popleft()

# iteration = N - K + 1

# out = []

# for i in range(iteration):
#     out.append(min(arr[i+2:i+K+2]))

# out = list(map(str, out))

# sys.stdout.write((" ".join(out)))


import sys
from collections import deque

# Чтение входных данных
data = list(map(int, sys.stdin.read().split()))
N, K = data[0], data[1]
arr = data[2:]

# Дек для хранения индексов потенциальных минимумов
dq = deque()
out = []

for i in range(N):
    # Убираем из конца элементы, которые больше текущего
    while dq and arr[dq[-1]] > arr[i]:
        dq.pop()
    
    dq.append(i)
    
    # Убираем элементы, которые вышли за окно
    if dq[0] <= i - K:
        dq.popleft()
    
    # Добавляем минимум текущего окна в результат
    if i >= K - 1:
        out.append(str(arr[dq[0]]))

# Вывод результата
sys.stdout.write(" ".join(out))
