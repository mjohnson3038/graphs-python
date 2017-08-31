import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_unittest(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_push(self):
        self.setUp()
        preCount = len(self.queue.elements)
        ele = "new element"

        self.assertTrue(self.queue.push(ele))

        postCount = len(self.queue.elements)
        self.assertEqual(self.queue.elements[postCount - 1], ele)

    def test_peek(self):
        self.setUp()

        self.assertIsNone(self.queue.peek())

        self.queue.push("Im something")
        prePeek = len(self.queue.elements)
        self.assertEqual("Im something", self.queue.peek())
        postPeek = len(self.queue.elements)

        self.assertEqual(prePeek, postPeek)

def main():
  unittest.main()

if __name__ == '__main__':
  main()
