class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed

        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_list(self):
        for node in self.nodes:
            print(node, '->', self.adj_list[node])

    def add_edge(self, u,v):
        self.adj_list[u].append(v)
        if self.is_directed:
            self.adj_list[v].append(u)

    def degree(self,node):



if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E"]
    graph = Graph(nodes, is_directed=True)


    graph.add_edge("A","B")
    graph.print_adj_list()