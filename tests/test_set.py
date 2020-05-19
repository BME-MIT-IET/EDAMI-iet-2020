from algorithms.set import (
    find_keyboard_row,
    RandomizedSet,
)

import random
import unittest

class TestFindKeyboardRow(unittest.TestCase):
    def test_find_keyboard_row(self):
        self.assertEqual(["Alaska", "Dad"],
                         find_keyboard_row(["Hello", "Alaska", "Dad", "Peace"]))

class TestRandomizedSet(unittest.TestCase):
    def test_insert_and_remove(self):
        rset = RandomizedSet()
        ground_truth = set()
        n = 64
    
        for i in range(n):
            rset.insert(i)
            ground_truth.add(i)
    
        # Remove a half
        for i in random.sample(range(n), n // 2):
            rset.remove(i)
            ground_truth.remove(i)
    
        print(len(ground_truth), len(rset.elements), len(rset.index_map))
        for i in ground_truth:
            self.assertEqual(i, rset.elements[rset.index_map[i]])
