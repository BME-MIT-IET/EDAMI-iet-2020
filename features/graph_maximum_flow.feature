Feature: Graph maximum flow

	Scenario: Graph 1
		Given these connections
			| 0 | 10 | 10 | 0 | 0 | 0 | 0  |
			| 0 | 0  | 2  | 0 | 4 | 8 | 0  |
			| 0 | 0  | 0  | 0 | 0 | 9 | 0  |
			| 0 | 0  | 0  | 0 | 0 | 0 | 0  |
			| 0 | 0  | 0  | 0 | 0 | 0 | 10 |
			| 0 | 0  | 0  | 0 | 6 | 0 | 10 |
			| 0 | 0  | 0  | 0 | 0 | 0 | 0  |
		Then the maximum flow from 0 to 6 with ford fulkerson is 19
		Then the maximum flow from 0 to 6 with edmonds karp is 19
		Then the maximum flow from 0 to 6 with dinic is 19

	Scenario: Graph 2
		Given these connections
			| 0 | 16 | 13 | 0  | 0  | 0  |
			| 0 | 0  | 10 | 12 | 0  | 0  |
			| 0 | 4  | 0  | 0  | 14 | 0  |
			| 0 | 0  | 9  | 0  | 0  | 20 |
			| 0 | 0  | 0  | 7  | 0  | 4  |
			| 0 | 0  | 0  | 0  | 0  | 0  |
		Then the maximum flow from first to last using BFS is 23
		Then the maximum flow from first to last using DFS is 23
