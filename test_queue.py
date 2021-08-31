from unittest import TestCase
from double_ended_queue import Deq
from queue_example import Queue
from stack import Stack
from circular_buffer import CB
import pytest


class TestQueueExample(TestCase):
    @pytest.mark.skip
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
