class LinkedList:
    def __init__(self, head = None):
        if head == None:
            self.head = None
        else:
            self.head = head

    def add_node(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            last = current
            last.next = newNode

    def length(self):
        if self.head == None:
            return 0
        else:
            current = self.head
            count = 0
            while current != None:
                current = current.next
                count += 1

            # current = last node here
            return count

    def reverse(self):
        current = self.head
        before = None
        after = None

        if (self.head is None) | (self.head.next is None):
            return True
        else:
            while (current is not None):
                after = current.next
                current.next = before
                before = current
                current = after
            self.head = before
            return LinkedList(self.head)

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next = None
