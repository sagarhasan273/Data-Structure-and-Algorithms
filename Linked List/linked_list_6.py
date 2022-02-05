# Before Head Addition of Linked List...

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class SLinkedList:
    def __init__(self):
        self.head = Node
    
    def print_list(self):
        temp = self.head
        while temp:
            print(f"-> {temp.data}")
            temp = temp.next
    
    def addition_before_head(self, new_val):
        temp = self.head
        new_head = Node(new_val)
        new_head.next = temp
        self.head = new_head

l_list = SLinkedList()
l_list.head = Node("Sunday")
mon = Node("Monday")
tues = Node("Tuesday")
wed = Node("Wednesday")
thur = Node("Thursday")
fri = Node("Friday")

l_list.head.next = mon
mon.next = tues
tues.next = wed
wed.next = thur
thur.next = fri

l_list.print_list()
l_list.addition_before_head("Saturday")
print()
l_list.print_list()

