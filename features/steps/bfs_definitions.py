from behave import *
from algorithms.bfs import count_islands
from algorithms.bfs import maze_search
from algorithms.bfs import ladder_length


@given('this grid')
def step_impl(context):
	if context.table:
		context.grid = [
			[int(cell) for cell in context.table.headings],
			*[[int(cell) for cell in row.cells] for row in context.table.rows]
		]
	else:
		context.words = []


@given('these words')
def step_impl(context):
	if context.table:
		context.words = list(context.table.headings)
		for row in context.table.rows:
			context.words.extend(row.cells)
	else:
		context.words = []


@when('I count the islands on the grid')
def step_impl(context):
	context.islands = count_islands(context.grid)


@then('there are {count:d} islands')
def step_impl(context, count):
	assert context.islands == count


@when('I search for the path on the grid')
def step_impl(context):
	context.path_length = maze_search(context.grid)


@then('the path is {length:d} steps long')
def step_impl(context, length):
	assert context.path_length == length


@then('no path is found')
def step_impl(context):
	assert context.path_length == -1


@when('I search for the ladder from {begin} to {end} through the words')
def step_impl(context, begin, end):
	context.ladder_length = ladder_length(begin, end, context.words)


@then('the ladder is {length:d} steps long')
def step_impl(context, length):
	assert context.ladder_length == length


@then('no ladder is found')
def step_impl(context):
	assert context.ladder_length == -1
