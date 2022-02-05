# After Addition of Linked List...

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
    
    def delection(self, val):
        temp = self.head
        while temp:
            if temp.data == val: 
                prev.next = temp.next
                break

            prev = temp
            temp = temp.next
    
    def addition_after(self, after, new_val):
        temp = self.head
        while temp:
            if temp.data == after:
                new = Node(new_val)
                new.next = temp.next
                temp.next = new
                break
            
            temp = temp.next

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
l_list.delection("Wednesday")
print()
l_list.print_list()
l_list.addition_after("Tuesday", "Wednesday")
l_list.addition_after("Friday", "Saturday")
print()
l_list.print_list()


