class Queue:

    def __init__(self):
        self.elements = []

    def push(self, ele):
        self.elements.append(ele)
        return True
