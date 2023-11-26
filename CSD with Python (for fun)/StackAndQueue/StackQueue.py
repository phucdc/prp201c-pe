stack = []
queue = []
# append new elements
for i in range(1, 6):
    stack.append(i)
    queue.append(i)

# pop vs dequeue
for i in range(1, 6):
    print(stack.pop(), end = " ")
print()
for i in range(1, 6):
    print(queue.pop(0), end = " ")