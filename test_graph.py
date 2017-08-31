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




def main():
  unittest.main()

if __name__ == '__main__':
  main()
