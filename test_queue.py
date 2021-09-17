from unittest import TestCase
from double_ended_queue import Deq
from queue_example import Queue
from stack import Stack
from circular_buffer import CB
from binary_tree import BinaryTree
from bucket_sort import bucket_sort
from bucket_sort import bucket_sort_alternative_version
import pytest
import random
import time


class TestQueueExample(TestCase):
    def test_appending_funk(self, a):
        test_queue = Queue()
        a_count = a
        for i in range(a_count):
            test_queue.appending_item(i)
        res = test_queue.print_out()
        assert res == [x for x in range(a_count)]

    def test_delete_funk(self):
        test_queue = Queue()
        test_queue.appending_item(10)
        test_queue.appending_item(20)
        test_queue.delete_item()
        res = test_queue.print_out()
        assert res == [10]


class TestDEQ(TestCase):
    def test_funk_deq_append_to_start(self):
        test_deq = Deq()
        test_deq.appending_to_start(100)
        res = test_deq.print_out()
        assert res == [100]

    def test_funk_deq_delete_first_item(self):
        test_deq = Deq()
        test_deq.appending_to_start(100)
        test_deq.appending_to_start(200)
        test_deq.delete_first_item()
        res = test_deq.print_out()
        assert res == [100]

    def test_funk_deq_delete_last_item(self):
        test_deq = Deq()
        test_deq.appending_to_start(100)
        test_deq.appending_to_start(200)
        test_deq.delete_last_item()
        res = test_deq.print_out()
        assert res == [200]

    def test_funk_deq_append_to_end(self):
        test_deq = Deq()
        test_deq.appending_item_to_end(100)
        test_deq.appending_item_to_end(200)
        res = test_deq.print_out()
        assert res == [100, 200]


class TestStack(TestCase):
    def test_stack_funk_append(self):
        test_stack = Stack()
        test_stack.appending_item(123)
        res = test_stack.print_out()
        assert res == [123]

    def test_stack_funk_delete(self):
        test_stack = Stack()
        test_stack.appending_item(321)
        test_stack.appending_item(3221)
        test_stack.delete_item()
        res = test_stack.print_out()
        assert res == [321]


class TestCB(TestCase):
    def test_cb_funk_appending(self):
        test_cb = CB(8)
        for i in range(1, 14):
            test_cb.appending_item(i)
        res = test_cb.print_out()
        assert res == [9, 10, 11, 12, 13, 6, 7, 8]

    def test_cb_funk_delete(self):
        test_cb = CB(8)
        for i in range(1, 14):
            test_cb.appending_item(i)
        test_cb.delete_item()
        res = test_cb.print_out()
        assert res == [9, 10, 11, 12, 13, None, 7, 8]


class TestBT(TestCase):
    def test_binary_tree_search(self):
        test_tree = BinaryTree(40)
        elements = [10, 30, 50, 60, 70, 55]
        for i in elements:
            test_tree.insert(i)
        res1 = test_tree.search_data(30)
        res = test_tree.search_data(100)
        assert res is False
        assert res1 is True

    def test_preorder_and_inorder_traverse_tree(self):
        test_tree = BinaryTree(40)
        elements = [10, 30, 50, 60, 70, 55]
        for i in elements:
            test_tree.insert(i)
        res1 = test_tree.preorder_traverse(test_tree)
        res = test_tree.inorder_traverse(test_tree)
        assert res1 == [40, 10, 30, 50, 60, 55, 70]
        assert res == [10, 30, 40, 50, 55, 60, 70]


class Test_bucket_sort_time(TestCase):
    def test_bucket_sort_time_with_alternative_sort(self):
        res = time.time()
        for x in range(10):
            my_list = [random.randint(100, 1000) for x in range(1, 1000)]
            bucket_sort(my_list, 5)
        result_sort = (time.time() - res) / 100
        res1 = time.time()
        for x in range(10):
            my_list = [random.randint(100, 1000) for x in range(1, 1000)]
            bucket_sort_alternative_version(my_list, 5)
        result_alternative_sort = (time.time() - res1) / 100
        assert result_sort < result_alternative_sort

