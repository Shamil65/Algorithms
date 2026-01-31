# class Stack():
#     def __init__(self):
#         self.inner_list = []

#     # def push(self, item):
#     #     carrent_min = self.min_el()
#     #     carrent_min = min(carrent_min, item)
#     #     self.inner_list.append((item, carrent_min))

#     # def len(self):
#     #     return len(self.inner_list)

#     def pop(self):
#         assert len(self.inner_list) != 0
#         removed_item = self.inner_list.pop()
#         return removed_item[0]

#     # def min_el(self):
#     #     if len(self.inner_list) == 0:
#     #         return 999999999
#     #     return self.inner_list[-1][1]


# # class QueueOnStacks():
# #     def __init__(self):
# #         self.s1 = Stack()
# #         self.s2 = Stack()

# #     def push(self, item):    
# #         self.s1.push(item)

# #     def pop(self):
# #         if self.s2.len() == 0:
# #             assert self.s1.len() > 0
# #             while self.s1.len() > 0:
# #                 item = self.s1.pop()
# #                 self.s2.push(item)

# #         return self.s2.pop()




# # queue = Stack()
# # queue.push(5)
# # queue.push(2)
# # queue.push(3)
# # queue.push(4)
# # queue.push(1)

# # print(queue.min_el())
# # queue.pop()

# # print(queue.min_el())
# # queue.pop()

# # print(queue.min_el())
# # queue.pop()

# # print(queue.min_el())
# # queue.pop()

# # print(queue.min_el())
# # queue.pop()



# class Stack():
#     def __init__(self):
#         self.inner_list =[]

#     def push(self, item):
#         min_element = self.get_min_el()
#         min_element = min(item, min_element)
#         self.inner_list.append((item, min_element))
        
#     def pop(self):
#         return self.inner_list.pop()

#     def get_min_el(self):
#         if len(self.inner_list) == 0:
#             return float('inf')
#         return self.inner_list[-1][1]


# stack1 = Stack()
# stack1.push(5)
# stack1.push(2)
# stack1.push(3)

# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print("Пиздец ахуительно")

print(len([0, 2, 1]))