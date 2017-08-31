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

    def test_pop(self):
        self.setUp()
        self.queue.push("I'm in the queue")
        self.queue.push("Butterfly")

        prePopCount = len(self.queue.elements)
        firstElement = self.queue.elements[0]
        self.assertEqual(firstElement, self.queue.pop())

        postPopCount = len(self.queue.elements)
        self.assertEqual(prePopCount - 1, postPopCount)

    def test_pop_on_empty_queue(self):
        self.setUp()

        prePopCount = len(self.queue.elements)

        self.assertIsNone(self.queue.pop())

        postPopCount = len(self.queue.elements)
        self.assertEqual(prePopCount, postPopCount)


def main():
  unittest.main()

if __name__ == '__main__':
  main()
