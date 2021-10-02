"""Dijkstra's shortest path algorithm implementation with directed and undirected graphs."""

import sys
import heapq
from typing import Union

from .edge_weighted_directed_graph import EdgeWeightedDirectedGraph
from .edge_weighted_undirected_graph import EdgeWeightedUndirectedGraph


def find_shortest_path_in_graph_with_queue(
    graph: Union[EdgeWeightedUndirectedGraph, EdgeWeightedDirectedGraph],
    source_vertex_key: Union[str, int],
):
    """Finds the shortest path from provided source vertex to every other vertex in the graph in an optimised way using min priority queues."""

    # Set the distance and predecessor for all the vertices to infinity and none
    distances = {vertex: sys.maxsize for vertex, _ in graph.vertices.items()}

    # Set distance for source vertex to 0
    distances[source_vertex_key] = 0

    # Setup a queue
    queue = [(0, source_vertex_key)]

    while len(queue) > 0:
        current_weight, current_vertex = heapq.heappop(queue)

        if current_weight > distances[current_vertex]:
            continue

        vertex = graph.vertices.get(current_vertex)
        adjacent_vertices = vertex.adjacent_vertices

        for vtx, weight in adjacent_vertices.items():

            calculated_weight = current_weight + weight
            if calculated_weight < distances[vtx.data]:
                distances.update({vtx.data: calculated_weight})
                heapq.heappush(queue, (calculated_weight, vtx.data))

    return distances


def run():
    """Run the algorithm implementation"""

    # Dijkstra shortest path in an undirected graph
    undirected_graph = EdgeWeightedUndirectedGraph()
    vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    edges = [
        (0, 1, 4),
        (0, 4, 8),
        (1, 2, 8),
        (1, 4, 11),
        (2, 3, 7),
        (2, 6, 4),
        (2, 8, 2),
        (3, 6, 14),
        (3, 7, 9),
        (4, 5, 1),
        (4, 8, 7),
        (5, 6, 2),
        (5, 8, 6),
        (6, 7, 10),
    ]

    for vertex in vertices:
        undirected_graph.add_vertex(vertex)

    for edge in edges:
        undirected_graph.add_edge_between_vertices(
            from_vertex_key=edge[0], to_vertex_key=edge[1], weight=edge[2]
        )

    print("Edge weighted undirected graph")
    distances = find_shortest_path_in_graph_with_queue(
        graph=undirected_graph, source_vertex_key=0
    )
    print(distances)

    # Dijkstra shortest path in an directed graph
    directed_graph = EdgeWeightedDirectedGraph()
    vertices = ["a", "b", "c", "d", "e"]
    edges = [
        ("a", "b", 10),
        ("b", "d", 1),
        ("a", "c", 5),
        ("c", "b", 3),
        ("c", "d", 9),
        ("c", "e", 2),
        ("e", "a", 2),
    ]

    for vertex in vertices:
        directed_graph.add_vertex(vertex)

    for edge in edges:
        directed_graph.add_edge_between_vertices(
            from_vertex_key=edge[0], to_vertex_key=edge[1], weight=edge[2]
        )

    print("\n")

    print("Edge weighted directed graph")
    distances = find_shortest_path_in_graph_with_queue(
        graph=directed_graph, source_vertex_key="a"
    )
    print(distances)
