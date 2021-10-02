"""Build graph from given vertices and edges."""
from __future__ import annotations


class Vertex:
    """Represents a vertex of graph."""

    def __init__(self, data) -> None:
        """Instantiate an instance of graph vertex."""
        self.data = data
        self.adjacent_vertices = {}

    def add_adjacent(self, vertex: Vertex, weight: int):
        """Add adjacent vertex to the current vertex."""
        self.adjacent_vertices.update({vertex: weight})

    def get_adjacent_vertices(self):
        """Get all the adjacent vertices for the current vertex."""
        return self.adjacent_vertices


class EdgeWeightedDirectedGraph:
    """Represents a graph of vertices and edges."""

    def __init__(self) -> None:
        """Instantiate an instance of graph."""
        self.vertices = dict()

    def add_vertex(self, data: str):
        """Add vertex to the graph."""
        self.vertices.update({data: Vertex(data=data)})

    def add_edge_between_vertices(
        self, from_vertex_key: str, to_vertex_key: str, weight: int
    ):
        """Add an edge connecting two vertices with a weight."""

        if (
            self.vertices.get(from_vertex_key, None) is None
            or self.vertices.get(to_vertex_key, None) is None
        ):
            raise Exception("Trying to add edge between non-existent vertices")

        fv = self.vertices.get(from_vertex_key)
        tv = self.vertices.get(to_vertex_key)

        fv.add_adjacent(tv, weight)

    def get_adjacent_vertices_for_vertex(self, vertex_key: str):
        """Get all the adjacent vertices for given vertex key."""

        vertex = self.vertices.get(vertex_key, None)
        if vertex is None:
            raise Exception("Provided vertex is unavailable in graph.")

        return vertex.get_adjacent_vertices()


if __name__ == "__main__":

    vertices = ["a", "b", "c", "d", "e"]
    graph = EdgeWeightedDirectedGraph()

    for vertex in vertices:
        graph.add_vertex(vertex)

    edges = [
        ("a", "b", 5),
        ("b", "c", 3),
        ("a", "d", 2),
        ("b", "d", 6),
        ("c", "e", 4),
        ("d", "e", 8),
    ]

    for edge in edges:
        graph.add_edge_between_vertices(
            from_vertex_key=edge[0], to_vertex_key=edge[1], weight=edge[2]
        )

    for vertex in vertices:
        adjacent_vertices = graph.get_adjacent_vertices_for_vertex(vertex_key=vertex)

        if len(adjacent_vertices.keys()) == 0:
            print(f"{vertex} has no adjacent vertices.")
        else:
            for adj_vertex, weight in adjacent_vertices.items():
                print(
                    f"{vertex} -> {adj_vertex.data} with weight for edge set to {weight}"
                )
