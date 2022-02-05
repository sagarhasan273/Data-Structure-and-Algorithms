class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None


l_list = SLinkedList()
l_list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

l_list.head.next = second
second.next = third
third.next = fourth.next

pointer = l_list.head
while pointer is not None:
    print(f"-> {pointer.data}")
    pointer = pointer.next