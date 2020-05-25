Feature: BFS Maze search

	Scenario: Maze path in grid 1
		Given this grid
			| 1 | 0 | 1 | 1 | 1 | 1 |
			| 1 | 0 | 1 | 0 | 1 | 0 |
			| 1 | 0 | 1 | 0 | 1 | 1 |
			| 1 | 1 | 1 | 0 | 1 | 1 |
		When I search for the path on the grid
		Then the path is 14 steps long

	Scenario: Maze path in grid 2
		Given this grid
			| 1 | 0 | 0 |
			| 0 | 1 | 1 |
			| 0 | 1 | 1 |
		When I search for the path on the grid
		Then no path is found