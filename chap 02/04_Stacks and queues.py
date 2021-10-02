# ------------------------------------------------------------------------------------------------------------------------------------
# Stack : collection that supports push and pop operations
# Pushing an item onto the stack is a constant-time operation since it doesn't matter how many items are already on the stack
# We could take that stack and pop an item off to operate on it
# Queue: collection that supports adding and removing
# The queue structure supports adding and removing items
# ------------------------------------------------------------------------------------------------------------------------------------

# For example in empty stack and push iteams onto it

from collections import deque
MOH = []

MOH.append(1)
MOH.append(2)
MOH.append(3)
MOH.append(4)

print(MOH)

# pop an item

n = MOH.pop()
print(n)
print(MOH)

# For example in queue


b = deque()

b.append(1)
b.append(2)
b.append(3)
b.append(4)

print(b)

# Pop an item in queue

v = b.popleft()
print(v)
print(b)
