"""Build graph from given vertices and edges."""
from __future__ import annotations


class Vertex:
    """Represents a vertex of graph."""

    def __init__(self, data) -> None:
        """Instantiate an instance of graph vertex."""
        self.data = data
        self.adjacent_vertices = list()

    def add_adjacent(self, vertex: Vertex):
        """Add adjacent vertex to the current vertex."""

        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)

    def get_adjacent_vertices(self):
        """Get all the adjacent vertices for the current vertex."""

        return [vertex.data for vertex in self.adjacent_vertices]


class DirectedGraph:
    """Represents a graph of vertices and edges."""

    def __init__(self) -> None:
        """Instantiate an instance of graph."""
        self.vertices = dict()

    def add_vertex(self, data: str):
        """Add vertex to the graph."""
        self.vertices.update({data: Vertex(data=data)})

    def add_edge_between_vertices(self, from_vertex_key: str, to_vertex_key: str):
        """Add an edge connecting two vertices with a weight."""

        if (
            self.vertices.get(from_vertex_key, None) is None
            or self.vertices.get(to_vertex_key, None) is None
        ):
            raise Exception("Trying to add edge between non-existent vertices")

        fv = self.vertices.get(from_vertex_key)
        tv = self.vertices.get(to_vertex_key)

        fv.add_adjacent(tv)

    def get_adjacent_vertices_for_vertex(self, vertex_key: str):
        """Get all the adjacent vertices for given vertex key."""

        vertex = self.vertices.get(vertex_key, None)
        if vertex is None:
            raise Exception("Provided vertex is unavailable in graph.")

        adjacent_vertices = vertex.get_adjacent_vertices()
        if len(adjacent_vertices) > 0:
            print(f"Adjacent vertices for {vertex_key}")
            print(adjacent_vertices)
        else:
            print(f"Vertex {vertex_key} has no adjacent vertices")


if __name__ == "__main__":

    vertices = ["a", "b", "c", "d", "e"]
    graph = DirectedGraph()

    for vertex in vertices:
        graph.add_vertex(vertex)

    edges = [
        ("a", "b"),
        ("b", "c"),
        ("a", "d"),
        ("b", "d"),
        ("c", "e"),
        ("d", "e"),
    ]

    for edge in edges:
        graph.add_edge_between_vertices(from_vertex_key=edge[0], to_vertex_key=edge[1])

    for vertex in vertices:
        graph.get_adjacent_vertices_for_vertex(vertex_key=vertex)
