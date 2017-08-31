class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, vertex):
        self.neighbors.append(vertex)

v1 = Vertex("one")
v2 = Vertex(2)

v1.add_neighbor(v2)

print v1.name
print v1.neighbors[0].name
