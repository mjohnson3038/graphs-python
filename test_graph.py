import unittest
from vertex import Vertex
from graph import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex("sample")
        self.graph = Graph()
        self.graph.add_vertex(self.vertex)


    def test_unittest(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_add_vertex_valid(self):
        pre_vertex_count = len(self.graph.verticies)

        validVertex = Vertex("valid")
        self.assertIsInstance(validVertex, Vertex)

        self.assertTrue(self.graph.add_vertex(validVertex))

        post_vertex_count = len(self.graph.verticies)
        self.assertEqual(pre_vertex_count + 1, post_vertex_count)
        self.assertIn(validVertex, self.graph.verticies)

    def test_add_vertext_not_valid(self):
        pre_vertex_count = len(self.graph.verticies)

        notValidVertex = "hello, I'm not valid"
        self.assertNotIsInstance(notValidVertex, Vertex)

        self.assertFalse(self.graph.add_vertex(notValidVertex))

        post_vertex_count = len(self.graph.verticies)
        self.assertEqual(pre_vertex_count, post_vertex_count)
        self.assertNotIn(notValidVertex, self.graph.verticies)

    def test_add_edge_between_valid_verticies(self):
        valid_vertex = Vertex("end")
        self.graph.add_vertex(valid_vertex)

        self.assertTrue(self.graph.add_edge(self.vertex, valid_vertex))
        self.assertIn(valid_vertex, self.vertex.neighbors)
        self.assertNotIn(self.vertex, valid_vertex.neighbors)

    def test_add_edge_but_start_vertex_not_in_graph(self):
        start_vertex = Vertex("start")
        self.assertFalse(self.graph.add_edge(start_vertex, self.vertex))
        self.assertNotIn(start_vertex, self.vertex.neighbors)
        self.assertNotIn(self.vertex, start_vertex.neighbors)

    def test_add_edge_but_end_vertex_not_in_graph(self):
        end_vertex = Vertex("start")
        self.assertFalse(self.graph.add_edge(self.vertex, end_vertex))
        self.assertNotIn(end_vertex, self.vertex.neighbors)
        self.assertNotIn(self.vertex, end_vertex.neighbors)

    def test_add_edge_but_start_vertex_not_vertext_object(self):
        start_vertex = "HeYYYY!!"

        self.assertNotIsInstance(start_vertex, Vertex)

        self.assertFalse(self.graph.add_edge(start_vertex, self.vertex))
        self.assertNotIn(start_vertex, self.vertex.neighbors)

    def test_add_edge_but_end_vertex_not_vertext_object(self):
        end_vertex = "HeYYYY!!"

        self.assertNotIsInstance(end_vertex, Vertex)

        self.assertFalse(self.graph.add_edge(self.vertex, end_vertex))
        self.assertNotIn(end_vertex, self.vertex.neighbors)

    def test_add_edge_but_neither_start_nor_end_vertex_are_vertext_object(self):
        start_vertex = "foo"
        end_vertex = "bar"

        self.assertNotIsInstance(start_vertex, Vertex)
        self.assertNotIsInstance(end_vertex, Vertex)
        self.assertFalse(self.graph.add_edge(self.vertex, end_vertex))

# TESTS to go along with teh shortest_path function
    # def test_distance_between_not_valid_verticies(self):
    #     self.setUp()
    #     not_valid_one = "Hello!"
    #     not_valid_two = "Bye"
    #
    #     self.assertFalse(self.graph.shortest_path(not_valid_one, not_valid_two))
    #     self.assertFalse(self.graph.shortest_path(self.vertex, not_valid_two))
    #     self.assertFalse(self.graph.shortest_path(not_valid_one, self.vertex))
    #
    # def test_shortest_path_both_verticies_must_be_on_graph(self):
    #     self.setUp()
    #     vertexNotOnGraph = Vertex("new")
    #
    #     self.assertFalse(self.graph.shortest_path(vertexNotOnGraph, self.vertex))
    #     self.assertFalse(self.graph.shortest_path(vertexNotOnGraph, vertexNotOnGraph))
    #     self.assertFalse(self.graph.shortest_path(self.vertex, vertexNotOnGraph))
    #
    # def test_shortest_path_between_the_same_verticies(self):
    #     self.setUp()
    #     self.assertEqual(0, self.graph.shortest_path(self.vertex, self.vertex))




def main():
  unittest.main()

if __name__ == '__main__':
  main()
