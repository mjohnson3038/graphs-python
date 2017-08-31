import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_unittest(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_push(self)
        self.setUp()
        preCount = len(self.queue)
        ele = "new element"

        self.assertTrue(self.queue.push(ele))

        postCount = len(self.queue)
        self.assertEqual(self.queue[postCount - 1], ele)

def main():
  unittest.main()

if __name__ == '__main__':
  main()
