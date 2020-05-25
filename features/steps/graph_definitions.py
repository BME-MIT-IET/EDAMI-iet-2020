from behave import *
from algorithms.graph import Tarjan, check_bipartite, ford_fulkerson, edmonds_karp, dinic, maximum_flow_bfs, \
	maximum_flow_dfs, all_pairs_shortest_path, bellman_ford, count_connected_number_of_component
from algorithms.graph.dijkstra import Dijkstra


@given('these edges')
def step_impl(context):
	if context.table:
		context.graph_edges = dict()
		for row in context.table.rows:
			context.graph_edges.setdefault(row['start'], []).append(row['end'])
	else:
		context.graph_edges = []


@given('these weighted edges')
def step_impl(context):
	if context.table:
		context.graph_weighted_edges = dict()
		for row in context.table.rows:
			context.graph_weighted_edges.setdefault(row['start'], dict())[row['end']] = float(row['weight'])
	else:
		context.graph_edges = []


@given('these connections')
def step_impl(context):
	if context.table:
		context.connections = [
			[float(cell) for cell in context.table.headings],
			*[[float(cell) for cell in row.cells] for row in context.table.rows]
		]
	else:
		context.connections = []


@when('I calculate the strongly connected components from the edges')
def step_impl(context):
	context.strongly_connected_components = Tarjan(context.graph_edges).sccs


@then('there is a strongly connected component with these nodes')
def step_impl(context):
	assert context.table

	nodes = list(context.table.headings)
	for row in context.table.rows:
		nodes.extend(row.cells)

	contains = False
	for component in context.strongly_connected_components:
		if component == nodes:
			contains = True
			break

	assert contains


@then('it is a bipartite graph')
def step_impl(context):
	assert check_bipartite(context.connections)


@then('it is not a bipartite graph')
def step_impl(context):
	assert not check_bipartite(context.connections)


@then('the lengths of the paths to each node from {start:d} is')
def step_impl(context, start):
	assert context.table

	lengths = list([int(cell) for cell in context.table.headings])
	for row in context.table.rows:
		lengths.extend([int(cell) for cell in row.cells])

	g = Dijkstra(len(context.connections))
	g.graph = context.connections
	assert g.dijkstra(start) == lengths


@then('the maximum flow from {start:d} to {end:d} with ford fulkerson is {max_flow:d}')
def step_impl(context, start, end, max_flow):
	assert ford_fulkerson(context.connections, start, end) == max_flow


@then('the maximum flow from {start:d} to {end:d} with edmonds karp is {max_flow:d}')
def step_impl(context, start, end, max_flow):
	assert edmonds_karp(context.connections, start, end) == max_flow


@then('the maximum flow from {start:d} to {end:d} with dinic is {max_flow:d}')
def step_impl(context, start, end, max_flow):
	assert dinic(context.connections, start, end) == max_flow


@then('the maximum flow from first to last using BFS is {max_flow:d}')
def step_impl(context, max_flow):
	assert maximum_flow_bfs(context.connections) == max_flow


@then('the maximum flow from first to last using DFS is {max_flow:d}')
def step_impl(context, max_flow):
	assert maximum_flow_dfs(context.connections) == max_flow


@then('the lengths of the shortest paths is')
def step_impl(context):
	assert context.table

	lengths = [
		[float(cell) for cell in context.table.headings],
		*[[float(cell) for cell in row.cells] for row in context.table.rows]
	]

	assert all_pairs_shortest_path(context.connections) == lengths


@then('there is a shortest path from {start}')
def step_impl(context, start):
	assert bellman_ford(context.graph_weighted_edges, start)


@then('the number of connected components is {components:d}')
def step_impl(context, components):
	graph = [
		[
			index
			for index, cell in enumerate(row)
			if cell > 0
		]
		for row in context.connections
	]

	assert count_connected_number_of_component.count_components(graph, len(graph) - 1) == components
