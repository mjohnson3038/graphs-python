from vertex import Vertex
from queue import Queue

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

# # WIP - change this to return the actual path using the linked list class constructed and a distcionary holding previous values.
#     def shortest_path(self, start, end):
#         if (not isinstance(start, Vertex)) | (not isinstance(end, Vertex)):
#             print "Start and end points must be valid indicies"
#             return False
#         elif (start not in self.verticies) | (end not in self.verticies):
#             print "Beginning and ending verticies must both be associated with the respected graph"
#             return False
#         elif (start == end):
#             # to return a linked list of just the single element
#             return True
#         else:
            # logic for the path
