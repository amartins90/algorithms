from algorithms.dijkstra import dijkstra


def test_dijkstra_simple_graph_1():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("D", 5)],
        "C": [("A", 2), ("D", 1), ("E", 7)],
        "D": [("B", 5), ("C", 1)],
        "E": [("C", 7)]
    }

    source_node = "A"

    distances = dijkstra(graph, "A")

    assert distances["A"] == 0
    assert distances["B"] == 4
    assert distances["C"] == 2
    assert distances["D"] == 3
    assert distances["E"] == 9

def test_dijkstra_simple_graph_2():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }

    distances = dijkstra(graph, "A")

    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == 3
    assert distances["D"] == 4
