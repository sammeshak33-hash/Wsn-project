import random


class SOARouting:

    def __init__(self, nodes, clusters):
        """
        Initialize SOA Routing.
        """

        self.nodes = nodes
        self.clusters = clusters
        self.routes = []

    def initialize_routes(self):
        """
        Initialize one route for each Cluster Head.
        """

        self.routes = []

        cluster_heads = list(self.clusters.keys())

        for ch in cluster_heads:

            route = [ch]

            self.routes.append(route)

        return self.routes

    def display_routes(self):
        """
        Display the initialized routes.
        """

        print("\n========== Initial Routes ==========\n")

        for i, route in enumerate(self.routes):

            print(f"Route {i + 1}")
            print(route)
            print("--------------------------------")