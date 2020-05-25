Feature: Graph check bipartite

	Scenario: Graph 1
		Given these connections
			| 0 | 0 | 1 |
			| 0 | 0 | 1 |
			| 1 | 1 | 0 |
		Then it is a bipartite graph

	Scenario: Graph 2
		Given these connections
			| 0 | 1 | 0 | 1 |
			| 1 | 0 | 1 | 0 |
			| 0 | 1 | 0 | 1 |
			| 1 | 0 | 1 | 0 |
		Then it is a bipartite graph

	Scenario: Graph 3
		Given these connections
			| 0 | 1 | 0 | 0 |
			| 1 | 0 | 1 | 1 |
			| 0 | 1 | 0 | 1 |
			| 0 | 1 | 1 | 0 |
		Then it is not a bipartite graph
