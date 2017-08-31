class LinkedList:
    def __init__(self, head = None):
        if head == None:
            self.head = None
        else:
            self.head = head

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



class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next = None

    def add_node(self, newNode):
        if self == None:
            self = newNode
        else:
            current = self
            while current.next != None:
                current = current.next
            last = current
            last.next = newNode
