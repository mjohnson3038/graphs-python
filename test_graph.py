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
        validVertex = Vertex("valid")
        pre_vertex_count = len(self.graph.verticies)
        self.assertTrue(self.graph.add_vertex(validVertex))
        post_vertex_count = len(self.graph.verticies)
        self.assertEqual(pre_vertex_count + 1, post_vertex_count)
        self.assertIn(validVertex, self.graph.verticies)



def main():
  unittest.main()

if __name__ == '__main__':
  main()
