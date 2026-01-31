# # n = int(input())
# # arr = list(map(int, input().split()))

# arr_1 = [4, 1, 3, 2]
# arr_tupik = []
# arr_2 = []

# # min_el = min(arr_1)
# # min_idx = arr_1.index(min_el)

# # print(min_idx)
# # for i in range(0, min_idx+1):
# #     arr_tupik.append(arr_1[i])
# # del arr_1[0:min_idx+1]


# # # arr_2.append(tupik_el)
# # tupik_el = arr_tupik.pop()

# # if not arr_2 or tupik_el == arr_2[-1] + 1:
# #     arr_2.append(tupik_el)
# #     del arr_2[-1]


    

# # print(arr_1[min_idx])

# while len(arr_1) != 0:
#     min_el = min(arr_1)
#     min_idx = arr_1.index(min_el)

#     print(min_idx)
#     for i in range(0, min_idx+1):
#         arr_tupik.append(arr_1[i])
#     del arr_1[0:min_idx+1]

#     tupik_el = arr_tupik.pop()
#     if not arr_2 or tupik_el == arr_2[-1] + 1:
#         arr_2.append(tupik_el)
#         del arr_2[-1]

#     # j = 0
#     # while True:
            
#     #     if not arr_2 or tupik_el == arr_2[-1] + 1:
#     #         arr_2.append(tupik_el)
#     #         del arr_2[-1]
#     #         j+=1
#     #     else:
#     #         break




# print(arr_tupik)
# print(arr_1)
# print(arr_2)

import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    wagons = list(map(int, data[1:1+n]))
    
    stack = []
    actions = []
    next_wagon = 1
    input_idx = 0
    
    while next_wagon <= n:
        if stack and stack[-1] == next_wagon:
            count = 0
            while stack and stack[-1] == next_wagon:
                stack.pop()
                next_wagon += 1
                count += 1
            actions.append((2, count))
        elif input_idx < n:
            count = 0
            while input_idx < n and wagons[input_idx] != next_wagon: # 3 2 1 4
                stack.append(wagons[input_idx]) # stack = [3, 2]
                input_idx += 1
                count += 1
            if input_idx < n:  # we found it
                stack.append(wagons[input_idx])
                input_idx += 1
                count += 1
            else:
                print(0)
                return
            actions.append((1, count))
        else:
            print(0)
            return
    
    print(len(actions))
    for action_type, k in actions:
        print(action_type, k)

if __name__ == "__main__":
    main()