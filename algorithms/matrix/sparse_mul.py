"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


# Python solution without table (~156ms):
def multiply(self, a, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if a is None or b is None:
        return None
    m, n, l = len(a), len(b[0]), len(b[0])
    if len(b) != n:
        raise Exception("A's column number must be equal to B's row number.")
    c = [[0 for _ in range(l)] for _ in range(m)]
    for i, row in enumerate(a):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in enumerate(b[k]):
                    if eleB: c[i][j] += eleA * eleB
    return c
