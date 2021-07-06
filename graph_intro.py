class Graph:
    def __init__(self, edge):
        self.edge = edge
        self.graph_dict = {}
        for start, end in self.edge:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dictionary Representation", self.graph_dict)

if __name__ == "__main__":

    # edge as tuple
    edge = [
        ("Phnom Penh", "Siem Reab"),
        ("Siem Reab", "Poi Pet"),
        ("Poi Pet", "Siem Reab"),
        ("Phnom Penh", "Poipet")
    ]

    # Create object
    graph = Graph(edge)



