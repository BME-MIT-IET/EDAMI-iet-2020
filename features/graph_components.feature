Feature: Graph components

	Scenario: Graph 1
		Given these connections
			| 0 | 0 | 1 | 0 | 0 | 0 |
			| 0 | 0 | 0 | 0 | 0 | 1 |
			| 1 | 0 | 0 | 0 | 1 | 0 |
			| 0 | 0 | 0 | 0 | 0 | 0 |
			| 0 | 0 | 1 | 0 | 0 | 0 |
			| 0 | 1 | 0 | 0 | 0 | 0 |
		Then the number of connected components is 3

	Scenario: Graph 2
		Given these connections
			| 0 |
		Then the number of connected components is 0

	Scenario: Graph 3
		Given these connections
			| 1 | 0 | 0 | 0 | 0 |
			| 0 | 0 | 0 | 0 | 0 |
			| 0 | 0 | 1 | 0 | 0 |
			| 0 | 0 | 0 | 1 | 0 |
			| 0 | 0 | 0 | 0 | 1 |
		Then the number of connected components is 4
