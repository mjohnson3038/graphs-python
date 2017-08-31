import unittest
from vertex import Vertex

class VertexTests(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex("sample")

    def test_unittest(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_add_valid_neighbor(self):
        self.setUp()
        validVertex = Vertex("valid")
        preNeighborCount = len(self.vertex.neighbors)
        self.assertTrue(self.vertex.add_neighbor(validVertex))
        postNeighborCount = len(self.vertex.neighbors)
        self.assertEqual(preNeighborCount + 1, postNeighborCount)
        self.assertIn(validVertex, self.vertex.neighbors)

    def test_add_neighbor_thats_int(self):
        self.setUp()
        preNeighborCount = self.vertex.neighbors.count
        notValidVertex = 12
        self.assertFalse(self.vertex.add_neighbor(notValidVertex))
        postNeighborCount = self.vertex.neighbors.count
        self.assertEqual(preNeighborCount, postNeighborCount)
        self.assertNotIn(notValidVertex, self.vertex.neighbors)

    def test_add_neighbor_thats_string(self):
        self.setUp()
        preNeighborCount = self.vertex.neighbors.count
        notValidVertex = "not valid"
        self.assertFalse(self.vertex.add_neighbor(notValidVertex))
        postNeighborCount = self.vertex.neighbors.count
        self.assertEqual(preNeighborCount, postNeighborCount)
        self.assertNotIn(notValidVertex, self.vertex.neighbors)

def main():
  unittest.main()

if __name__ == '__main__':
  main()
