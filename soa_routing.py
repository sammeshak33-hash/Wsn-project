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

    def select_male_female_snakes(self, fitness_values):
        """
        Select the Male Snake (best route) and
        Female Snake (second-best route).
        """

        ranked_routes = list(zip(self.routes, fitness_values))

        ranked_routes.sort(
            key=lambda x: x[1],
            reverse=True
        )

        male_snake = ranked_routes[0]
        female_snake = ranked_routes[1]

        return male_snake, female_snake             
    
    def snake_searching(self, route):
        """
        Exploration phase of SOA.
        Randomly selects a different Cluster Head.
        """

        new_route = route.copy()

        current_ch = new_route[0]

        # Available Cluster Heads
        candidate_heads = list(self.clusters.keys())

        if len(candidate_heads) > 1:

            new_ch = random.choice(candidate_heads)

            while new_ch == current_ch:

                new_ch = random.choice(candidate_heads)

            new_route[0] = new_ch

        return new_route