class Stack():
    def __init__(self):
        self.inner_list = []

    def push(self, item):
        self.inner_list.append(item)
        # print(self.inner_list)

    def pop(self):
        return self.inner_list.pop()

import sys

data = sys.stdin.read().split()
# print(data)

stack2 = Stack()

for i in data:
    # print(i)
    if i == '+':
        second = stack2.pop()
        first = stack2.pop()
        ans = first + second
        stack2.push(ans)
        # print(first + second)

    elif i == '-':
        second = stack2.pop()
        first = stack2.pop()
        ans = first - second
        stack2.push(ans)

        # print(first - second)

    elif i == '*':
        second = stack2.pop()
        first = stack2.pop()
        ans = first * second
        stack2.push(ans)

        # print(first * second)

    else:
        stack2.push(int(i))

print(stack2.pop())