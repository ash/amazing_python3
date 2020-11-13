# A Linked list keeps the items
# of the Node class.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def append(self, new_node):
        self.next = new_node

# Create a linked list of 5 items.
head = Node(10) # The head of the list
curr = head
for n in range(20, 60, 10):
    new_node = Node(n)
    curr.append(new_node)
    curr = new_node

# Print the items in the linked list.
curr = head
while curr:
    print(curr.value, '-> ', end='')
    curr = curr.next
print('END')

# Output:
# 10 -> 20 -> 30 -> 40 -> 50 -> END
