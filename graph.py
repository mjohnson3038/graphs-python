from vertex import Vertex

class Graph:

    def __init__(self):
        self.verticies = set()

    def add_vertex(self, vertex):
        if (not isinstance(vertex, Vertex)):
            print "You can only add valid vertex objects to the graph. Try again"
            return False
        else:
            self.verticies.add(vertex)
            return True

    # NOTE - an edge only goes one direction.
    def add_edge(self, start, end):
        if (start not in self.verticies) | (end not in self.verticies):
            print "Add the vertex to the graph before creating an edge on it"
            return False
        elif (not isinstance(start, Vertex)) | (not isinstance(end, Vertex)):
            print "Start and edge points must both be verticies"
            return False
        else:
            start.add_neighbor(end)
            return True


v1 = Vertex(1)
v2 = Vertex(2)

g = Graph()
g.add_vertex(v1)
g.add_vertex(v2)

g.add_edge(v1, v2)

# print v1.neighbors
# print type(v2)
# print type(g)
print isinstance(v1, Vertex)
