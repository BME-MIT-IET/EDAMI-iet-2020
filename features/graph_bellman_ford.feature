Feature: Graph bellman ford

	Scenario: Graph 1
		Given these weighted edges
			| start | end | weight |
			| a     | b   | 6      |
			| a     | e   | 7      |
			| b     | c   | 5      |
			| b     | d   | -4     |
			| b     | e   | 8      |
			| c     | b   | -2     |
			| d     | a   | 2      |
			| d     | c   | 7      |
			| e     | b   | -3     |
		Then there is a shortest path from a

	Scenario: Graph 2
		Given these weighted edges
			| start | end | weight |
			| a     | d   | 3      |
			| a     | e   | 4      |
			| b     | a   | 7      |
			| b     | e   | 2      |
			| c     | a   | 12     |
			| c     | d   | 9      |
			| c     | e   | 11     |
			| d     | c   | 5      |
			| d     | e   | 11     |
			| e     | a   | 7      |
			| e     | b   | 5      |
			| e     | d   | 1      |
		Then there is a shortest path from a
