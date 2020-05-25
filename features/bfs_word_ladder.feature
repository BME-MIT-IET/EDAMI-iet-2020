Feature: BFS Ladder length

	Scenario: Ladder in words 1
		Given these words
			| hot | dot | dog | lot | log |
		When I search for the ladder from hit to cog through the words
		Then the ladder is 5 steps long

	Scenario: Ladder in words 2
		Given these words
			| tock | tick | sank | sink | sick |
		When I search for the ladder from pick to tank through the words
		Then the ladder is 5 steps long

	Scenario: Ladder in words 3
		Given these words
			| hoho | luck |
		When I search for the ladder from live to life through the words
		Then the ladder is 1 steps long

	Scenario: Ladder in words 4
		Given these words
		When I search for the ladder from ate to ate through the words
		Then the ladder is 0 steps long

	Scenario: Ladder in words 5
		Given these words
			| blahh | blhah |
		When I search for the ladder from rahul to coder through the words
		Then no ladder is found
