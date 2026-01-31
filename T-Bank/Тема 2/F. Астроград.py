# import sys


# class Queue():
#     def __init__(self):
#         self.inner_list = []

#     def push(self, item): # 1. В очередь пришел новый человек с уникальным номером id, он встает в очередь последним.
#         self.inner_list.append(item)

#     def buy(self): # 2. Человеку, стоящему спереди в очереди, удалось купить билет. Он уходит.
#         return self.inner_list.pop(0)
    
#     def tired(self): # 3. Человеку, стоящему последнему в очереди, надоело ждать. Он уходит.
#         return self.inner_list.pop()
    
#     def people_ahead(self, id): # 4. Человек с уникальным номером q хочет знать, сколько людей стоит в очереди спереди него.
#         idx = self.inner_list.index(id)
#         return len(self.inner_list[0:idx])

#     def delays(self): # 5. Очередь хочет знать, человек с каким уникальным номером стоит сейчас первым и задерживает всех.
#         return self.inner_list[0]

    
# Queue1 = Queue()

# # Queue1.push(1)
# # print(Queue1.delays()) #
# # Queue1.push(3)
# # Queue1.tired()
# # Queue1.buy()
# # Queue1.push(2)
# # print(Queue1.people_ahead(2)) #


# data = [line.split() for line in sys.stdin]
# data = data[1:]
# # print(data)


# for i in data:
#     if i[0] == '1':
#         Queue1.push(i[1])
#     elif i[0] == '2':
#         Queue1.buy()
#     elif i[0] == '3':
#         Queue1.tired()
#     elif i[0] == '4':
#         print(Queue1.people_ahead(i[1]))
#     elif i[0] == '5':
#         print(Queue1.delays())
import sys


class Queue:
    def __init__(self):
        self.arr = []
        self.head = 0
        self.pos = {}   # id -> index in arr

    def push(self, id):
        self.pos[id] = len(self.arr)
        self.arr.append(id)

    def buy(self):
        id = self.arr[self.head]
        del self.pos[id]
        self.head += 1

    def tired(self):
        id = self.arr.pop()
        del self.pos[id]

    def people_ahead(self, id):
        return self.pos[id] - self.head

    def delays(self):
        return self.arr[self.head]


queue = Queue()

data = sys.stdin.read().splitlines()[1:]

for line in data:
    cmd = line.split()
    if cmd[0] == '1':
        queue.push(cmd[1])
    elif cmd[0] == '2':
        queue.buy()
    elif cmd[0] == '3':
        queue.tired()
    elif cmd[0] == '4':
        print(queue.people_ahead(cmd[1]))
    elif cmd[0] == '5':
        print(queue.delays())
