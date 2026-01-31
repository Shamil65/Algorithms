import sys

class Stack():
    def __init__(self):
        self.inner_list = []

    def push(self, item):
        min_element = self.get_min_el()
        min_element = min(min_element, item)
        self.inner_list.append((item, min_element))

    def pop(self):
        return self.inner_list.pop()

    def get_min_el(self):
        if len(self.inner_list) == 0:
            return float('inf')
        return self.inner_list[-1][1]

    def view_stack(self):
        print(self.inner_list)

    def view_min_el(self):
        return self.inner_list[-1][1]

# stack1 = Stack()
# stack1.push(3)
# stack1.push(2)
# stack1.push(1)

# stack1.view_stack()
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())


def main():
    data = sys.stdin
    # print(data)
    t = int(data.readline())

    stack = Stack()
    out = []

    for _ in range(t):
        op = data.readline().split()
        cmd = int(op[0])

        if cmd == 1:          # push
            stack.push(int(op[1]))
        elif cmd == 2:        # pop
            stack.pop()
        elif cmd == 3:        # get min
            out.append(str(stack.get_min_el()))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
