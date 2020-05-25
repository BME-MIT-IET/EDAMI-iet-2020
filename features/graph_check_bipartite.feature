Feature: Graph tarjan

	Scenario: Graph 1
		Given these edges
			| start | end |
			| A     | B   |
			| B     | C   |
			| B     | E   |
			| B     | F   |
			| C     | D   |
			| C     | G   |
			| D     | C   |
			| D     | H   |
			| E     | A   |
			| E     | F   |
			| F     | G   |
			| G     | F   |
			| H     | D   |
			| H     | G   |
		When I calculate the strongly connected components from the edges
		Then there is a strongly connected component with these nodes
			| F | G |
		And there is a strongly connected component with these nodes
			| C | D | H |
		And there is a strongly connected component with these nodes
			| A | B | E |

	Scenario: Graph 2
		Given these edges
			| start | end |
			| A     | E   |
			| B     | A   |
			| C     | B   |
			| C     | D   |
			| D     | C   |
			| E     | B   |
			| F     | B   |
			| F     | E   |
			| F     | G   |
			| G     | F   |
			| G     | C   |
			| H     | G   |
			| H     | H   |
			| H     | D   |
		When I calculate the strongly connected components from the edges
		Then there is a strongly connected component with these nodes
			| A | B | E |
		And there is a strongly connected component with these nodes
			| C | D |
		And there is a strongly connected component with these nodes
			| F | G |
		And there is a strongly connected component with these nodes
			| H |
