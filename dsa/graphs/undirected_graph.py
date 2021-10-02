"""Undirected graph with no weights."""
from __future__ import annotations


class Vertex:
    """Representation of a vertex in undirected graph."""

    def __init__(self, data) -> None:
        """Instantiate vertex object."""
        self.data = data
        self.adjacent_vertices = list()

    def add_adjacent(self, vertex: Vertex) -> None:
        """Add adjacent vertex to the current vertex."""
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)

        # Adding the current vertex in the vertex's adjacent vertices list
        vertex.adjacent_vertices.append(self)

    def get_adjacent_vertices(self) -> list:
        """Return all the adjacent vertices of the given node."""

        return [vertex.data for vertex in self.adjacent_vertices]


class UndirectedGraph:
    """Representation of an undirected graph."""

    def __init__(self) -> None:
        """Instantiates undirected graph object."""
        self.vertices = dict()

    def add_vertex(self, data: str) -> None:
        """Adds vertex to the graph."""
        if self.vertices.get(data, None) is None:
            vertex = Vertex(data=data)
            self.vertices.update({data: vertex})

    def add_edge_between_vertices(
        self, from_vertex_key: str, to_vertex_key: str
    ) -> None:
        """Adds edge between given vertices."""

        if (
            self.vertices.get(from_vertex_key, None) is None
            or self.vertices.get(to_vertex_key, None) is None
        ):
            raise Exception("Trying to add edge between non-existent vertices")

        fv = self.vertices.get(from_vertex_key)
        tv = self.vertices.get(to_vertex_key)

        fv.add_adjacent(tv)

    def get_adjacent_vertices_for_vertex(self, vertex_key: str) -> list:
        """Get all the adjacent vertices for the given vertex key."""

        vertex = self.vertices.get(vertex_key, None)

        if vertex is None:
            raise Exception("Vertex is unavailable in the graph.")

        adjacent_vertices = vertex.get_adjacent_vertices()
        if len(adjacent_vertices) > 0:
            print(f"Adjacent vertices for {vertex_key}")
            print(adjacent_vertices)
        else:
            print(f"Vertex {vertex_key} has no adjacent vertices")


if __name__ == "__main__":

    vertices = ["a", "b", "c", "d", "e"]
    graph = UndirectedGraph()

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
