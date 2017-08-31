class Queue:

    def __init__(self):
        self.elements = []

    def push(self, ele):
        self.elements.append(ele)
        return True

    def peek(self):
        if len(self.elements) == 0:
            return None
        else:
            return self.elements[0]
