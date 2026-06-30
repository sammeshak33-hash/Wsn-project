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

    def calculate_route_fitness(self):
        """
        Calculate fitness for each routing path.
        """

        fitness_values = []

        for route in self.routes:

            ch = route[0]

            node = self.nodes[ch]

            distance = node.distance_to_bs
            trust = node.total_trust
            energy = node.energy

            fitness = (
                0.40 * (1 / distance)
                +
                0.35 * trust
                +
                0.25 * energy
            )

            fitness_values.append(fitness)

        return fitness_values


    def display_route_fitness(self, fitness_values):
        """
        Display route fitness values.
        """

        print("\n========== Route Fitness ==========\n")

        for i, fitness in enumerate(fitness_values):

            print(f"Route {i+1}")

            print("Fitness :", round(fitness, 6))

            print("--------------------------------")        