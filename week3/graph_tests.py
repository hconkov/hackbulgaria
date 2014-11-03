import unittest

from graph import Graph


class TestGraph(unittest.TestCase):

    def test_graph_constructor(self):
        new_graph = Graph("1", "2")
        self.assertEqual(new_graph.node, "1")
        self.assertEqual(new_graph.edge, "2")
        self.assertEqual(new_graph.nodedict, {})

    def test_add_edge(self):
        new_graph = Graph("1", "2")
        self.assertEqual(new_graph.node, "1")
        self.assertEqual(new_graph.edge, "2")
        self.assertEqual(new_graph.nodedict, {})
        new_graph.add_edge("1", "2")
        new_graph.add_edge("2", "3")
        self.assertEqual(new_graph.nodedict, {"1": ["2"], "2": ["3"], "3": []})

    def test_get_neighbours(self):
        new_graph = Graph("1", "2")
        self.assertEqual(new_graph.node, "1")
        self.assertEqual(new_graph.edge, "2")
        self.assertEqual(new_graph.nodedict, {})
        new_graph.add_edge("1", "2")
        new_graph.add_edge("2", "3")
        new_graph.add_edge("1", "3")
        self.assertEqual(
            new_graph.nodedict, {"1": ["2", "3"], "2": ["3"], "3": []})
        self.assertEqual(new_graph.get_neighbours("1"), ["2", "3"])

    def test_path(self):
        new_graph = Graph("1", "2")
        self.assertEqual(new_graph.node, "1")
        self.assertEqual(new_graph.edge, "2")
        self.assertEqual(new_graph.nodedict, {})
        new_graph.add_edge("1", "2")
        new_graph.add_edge("2", "3")
        self.assertEqual(new_graph.nodedict, {"1": ["2"], "2": ["3"], "3": []})
        self.assertTrue(new_graph.path_between("1", "3"))
        self.assertFalse(new_graph.path_between("3", "1"))


if __name__ == '__main__':
    unittest.main()
