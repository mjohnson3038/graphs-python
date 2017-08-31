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




def main():
  unittest.main()

if __name__ == '__main__':
  main()
