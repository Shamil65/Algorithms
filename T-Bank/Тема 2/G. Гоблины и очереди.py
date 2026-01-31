# + i − гоблин с номером i (1 6 i 6 N) встаёт в конец очереди.
# • * i − привилегированный гоблин с номером i встает в середину очереди.
# • - − первый гоблин из очереди уходит к шаманам. Гарантируется, что на момент такого запроса
# очередь не пуста.

# 7
# + 1
# + 2
# -
# + 3
# + 4
# -
# -
# =======
# 1
# 2
# 3

# 2
# * 1
# + 2
# =======
import sys

data = sys.stdin.read().split("\n")[:-2]
print(data)

N = data.pop(0)

class Gonlins_queue():
    def __init__(self):
        self.inner_list = []

    def add_ordinary_gonlin(self, goblin):
        self.inner_list.append(goblin)

    def add_primary_gonlin(self, gonlin):
        len_queue = len(self.inner_list)
        if len_queue % 2 == 0:
            self.inner_list
        else:
            pass