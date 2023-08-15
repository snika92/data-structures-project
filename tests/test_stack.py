"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, "data3")
        self.assertEqual(stack.top.next_node.data, "data2")
        self.assertEqual(stack.top.next_node.next_node.data, "data1")
        self.assertIsNone(stack.top.next_node.next_node.next_node)

        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        pop_test = stack.pop()
        self.assertEqual(pop_test, "data1")
        self.assertIsNone(stack.top)

        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        pop_test = stack.pop()
        self.assertEqual(stack.top.data, "data1")
        self.assertEqual(pop_test, "data2")

    def test_str(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')

        self.assertEqual(str(stack), "data1\ndata2")
