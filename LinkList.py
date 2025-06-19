# Manual Linked List Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        self.size += 1

    def delete_first(self):
        if not self.head:
            print("List is Empty.")
            return
        self.head = self.head.next
        self.size -= 1

    def delete_last(self):
        if not self.head:
            print("List is Empty.")
            return
        self.size -= 1
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        last = self.head.next
        while last.next:
            second_last = second_last.next
            last = last.next
        second_last.next = None

    def print_list(self):
        if not self.head:
            print("List is Empty.")
            return
        curr = self.head
        while curr:
            print(f"{curr.data} --> ", end="")
            curr = curr.next
        print("NULL")

    def print_size(self):
        print(f"\n\nSize of list is {self.size}")


# Testing Manual Linked List
print("Linked List Using Manual Code.")
list1 = LinkList()
list1.add_first(5)
list1.add_first(4)
list1.add_first(2)
list1.add_last(87)
list1.delete_first()
list1.delete_last()
list1.print_list()
list1.print_size()

# Using Python's built-in LinkedList from collections.deque
from collections import deque
print("\nUsing Linked List Collection Framework.")

str_list = deque()
str_list.appendleft("A")
str_list.append("B")
str_list.append("C")
print(list(str_list))
print(len(str_list))
for x in str_list:
    print(x, end=" --> ")
print("NULL")

str_list.append("D")
str_list.append("H")
str_list.insert(2, "E")
print(list(str_list))
str_list.popleft()
str_list.pop()
del str_list[0]
del str_list[1]
print(list(str_list))
print(str_list[1])
