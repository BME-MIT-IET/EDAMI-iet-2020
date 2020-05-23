from algorithms.set import (
    find_keyboard_row,
    greedy_set_cover,
    optimal_set_cover,
    powerset,
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

class TestSetCovering(unittest.TestCase):
    def test_powerset(self):
        self.assertEqual(
            list(powerset([1,2,3])),
            [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]
        )

    def test_set_cover(self):
        universe = {1, 2, 3, 4, 5}
        subsets = {'S1': {4, 1, 3}, 'S2': {2, 5}, 'S3': {1, 4, 3, 2}}
        costs = {'S1': 5, 'S2': 10, 'S3': 3}

        optimal_cover = optimal_set_cover(universe, subsets, costs)
        optimal_cost = sum(costs[s] for s in optimal_cover)
        self.assertEqual(optimal_cover, ('S2', 'S3'))
        self.assertEqual(optimal_cost, 13)

        greedy_cover = greedy_set_cover(universe, subsets, costs)
        greedy_cost = sum(costs[s] for s in greedy_cover)
        self.assertEqual(greedy_cover, ['S3', 'S2'])
        self.assertEqual(greedy_cost, 13)

    def test_set_no_cover(self):
        universe = {1, 2, 3, 4, 5}
        subsets = {'S1': {1, 3}, 'S2': {2, 5}, 'S3': {1, 3, 2}}
        costs = {'S1': 5, 'S2': 10, 'S3': 3}
        optimal_cover = optimal_set_cover(universe, subsets, costs)
        greedy_cover = greedy_set_cover(universe, subsets, costs)
        self.assertEqual(optimal_cover, None)
        self.assertEqual(greedy_cover, None)
