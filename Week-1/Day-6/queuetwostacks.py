import unittest
import queue

class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    s1 = queue.LifoQueue()
    s2 = queue.LifoQueue()

    def enqueue(self, item):
        self.s1.put(item)

    def dequeue(self):
        if(self.s1.qsize()==0):
            raise Exception("queue empty")
        else:
            while(self.s1.qsize()>1):
                self.s2.put(self.s1.get())
            temp = self.s1.get()
            while(self.s2.qsize()>0):
                self.s1.put(self.s2.get())
            return temp

# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()
