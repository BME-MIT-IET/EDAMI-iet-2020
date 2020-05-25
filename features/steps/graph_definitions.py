from behave import *
from algorithms.bfs import (
	count_islands,
	maze_search,
	ladder_length
)


@when('I count the islands on the grid')
def step_impl(context):
	context.islands = count_islands(context.grid)


@when('I search for the path on the grid')
def step_impl(context):
	context.path_length = maze_search(context.grid)


@when('I search for the ladder from {begin} to {end} through the words')
def step_impl(context, begin, end):
	context.ladder_length = ladder_length(begin, end, context.words)


@then('there are {count:d} islands')
def step_impl(context, count):
	assert context.islands == count


@then('the path is {length:d} steps long')
def step_impl(context, length):
	assert context.path_length == length


@then('no path is found')
def step_impl(context):
	assert context.path_length == -1


@then('the ladder is {length:d} steps long')
def step_impl(context, length):
	assert context.ladder_length == length


@then('no ladder is found')
def step_impl(context):
	assert context.ladder_length == -1
