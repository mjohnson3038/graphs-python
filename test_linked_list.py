import unittest
from linked_list import LinkedList
from linked_list import Node

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.head = Node(1, 1)
        self.linked_list = LinkedList(self.head)

    def test_unittest(self):
        self.assertTrue(True)
        self.assertFalse(False)


    def test_add_node(self):
        newNode = Node(1, 1)

        originalLength = self.linked_list.length()
        self.assertIsNone(self.head.next)

        self.linked_list.add_node(newNode)
        newLength = self.linked_list.length()
        self.assertEqual(self.head.next, newNode)
        self.assertEqual(originalLength + 1, newLength)

    def test_length(self):
        self.setUp()
        self.assertEqual(1, self.linked_list.length())

        newNode = Node(1, "Hi!")
        self.head.next = newNode

        self.assertEqual(2, self.linked_list.length())

    def test_length_of_empty_list(self):
        emptyLinkedList = LinkedList()
        self.assertEqual(0, emptyLinkedList.length())

    def test_reverse_on_empty_list(self):
        emptyLinkedList = LinkedList()
        self.assertEqual(None, emptyLinkedList.head)

    def test_reverse_on_list_of_one_element(self):
        self.setUp()
        original_head = self.head
        self.linked_list.reverse()
        self.assertEqual(original_head, self.head)

    def test_reverse(self):
        self.setUp()

        firstNewNode = Node(2, 2)
        secondNewNode = Node(5, 5)
        thirdNewNode = Node(6, 6)
        fourthNewNode = Node(8, 8)

        self.linked_list.add_node(firstNewNode)
        self.linked_list.add_node(secondNewNode)
        self.linked_list.add_node(thirdNewNode)
        self.linked_list.add_node(fourthNewNode)

        originalLength = self.linked_list.length()

        self.linked_list = self.linked_list.reverse()

        newLength = self.linked_list.length()

        self.assertEqual(originalLength, newLength)
        self.assertEqual(fourthNewNode, self.linked_list.head)
        self.assertEqual(1, self.linked_list.head.next.next.next.next.value)

class NodeTest(unittest.TestCase):
      def setUp(self):
          self.node = Node(0, 0)

def main():
  unittest.main()

if __name__ == '__main__':
  main()
