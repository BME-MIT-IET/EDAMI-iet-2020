Feature: BFS

	Rule: Island count

		Scenario: Islands in grid 1
			Given this grid
				| 1 | 1 | 1 | 1 | 0 |
				| 1 | 1 | 0 | 1 | 0 |
				| 1 | 1 | 0 | 0 | 0 |
				| 0 | 0 | 0 | 0 | 0 |
			When I count the islands
			Then there are 1 islands

		Scenario: Islands in grid 2
			Given this grid
				| 1 | 1 | 0 | 0 | 0 |
				| 1 | 1 | 0 | 0 | 0 |
				| 0 | 0 | 1 | 0 | 0 |
				| 0 | 0 | 0 | 1 | 1 |
			When I count the islands
			Then there are 3 islands

		Scenario: Islands in grid 2
			Given this grid
				| 1 | 1 | 1 | 0 | 0 | 0 |
				| 1 | 1 | 0 | 0 | 0 | 0 |
				| 1 | 0 | 0 | 0 | 0 | 1 |
				| 0 | 0 | 1 | 1 | 0 | 1 |
				| 0 | 0 | 1 | 1 | 0 | 0 |
			When I count the islands
			Then there are 3 islands

		Scenario: Islands in grid 2
			Given this grid
				| 1 | 1 | 0 | 0 | 1 | 1 |
				| 0 | 0 | 1 | 1 | 0 | 0 |
				| 0 | 0 | 0 | 0 | 0 | 1 |
				| 1 | 1 | 1 | 1 | 0 | 0 |
			When I count the islands
			Then there are 5 islands

	Rule: Maze search

		Scenario: Islands in grid 1
			Given this grid
				| 1 | 0 | 1 | 1 | 1 | 1 |
				| 1 | 0 | 1 | 0 | 1 | 0 |
				| 1 | 0 | 1 | 0 | 1 | 1 |
				| 1 | 1 | 1 | 0 | 1 | 1 |
			When I count the islands
			Then there are 1 islands

		Scenario: Islands in grid 2
			Given this grid
				| 1 | 0 | 0 |
				| 0 | 1 | 1 |
				| 0 | 1 | 1 |
			When I count the islands
			Then there are 3 islands