"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertIsNone(queue.tail.next_node)

        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)

    def test_str(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(str(queue), "data1\ndata2\ndata3")

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        pop_1 = queue.dequeue()
        self.assertEqual(pop_1, "data1")

        pop_2 = queue.dequeue()
        self.assertEqual(pop_2, "data2")

        pop_3 = queue.dequeue()
        self.assertEqual(pop_3, "data3")

        pop_4 = queue.dequeue()
        self.assertIsNone(pop_4)
