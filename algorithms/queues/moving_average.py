from __future__ import division
from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)
