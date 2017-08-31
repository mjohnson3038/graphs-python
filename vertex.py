class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, vertex):
        if not isinstance(vertex, Vertex):
            print "All neighbors must be vertex objects, try again."
            return False
        else:
            self.neighbors.append(vertex)
            return True

v1 = Vertex("one")
v2 = Vertex(2)

v1.add_neighbor(v2)
