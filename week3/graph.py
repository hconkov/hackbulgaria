class Graph:

    def __init__(self, node, edge):
        self.node = node
        self.edge = edge
        self.nodedict = {}

    def add_edge(self, node1, node2):
        if node1 not in self.nodedict:
            self.nodedict[node1] = []
        if node2 not in self.nodedict:
            self.nodedict[node2] = []
        if node2 not in self.nodedict[node1]:
            self.nodedict[node1].append(node2)

    def get_neighbours(self, node):
        if node in self.nodedict:
            return self.nodedict[node]
        else:
            return("No such node")

    def path_between(self, node1, node2):
        if node1 not in self.nodedict or node2 not in self.nodedict:
            return False
        elif node2 in self.get_neighbours(node1):
            return True
        for node in self.get_neighbours(node1):
            if self.path_between(node, node2):
                return True
        return False
