import unittest
from linked_list import LinkedList
from linked_list import Node

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.head = Node(1, 2)
        self.linked_list = LinkedList(self.head)

    def test_unittest(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_length(self):
        self.setUp()
        print self.linked_list
        self.assertEqual(1, self.linked_list.length())

        newNode = Node(1, "Hi!")
        self.head.next = newNode

        self.assertEqual(2, self.linked_list.length())

    def test_length_of_empty_list(self):
        emptyLinkedList = LinkedList()
        self.assertEqual(0, emptyLinkedList.length())


class NodeTest(unittest.TestCase):
      def setUp(self):
          self.node = Node(0, 0)

      def test_add_node(self):
          newNode = Node(1, 1)

          self.assertIsNone(self.node.next)

          self.node.add_node(newNode)
          self.assertEqual(self.node.next, newNode)





def main():
  unittest.main()

if __name__ == '__main__':
  main()
