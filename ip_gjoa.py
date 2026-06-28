import math
import random
from config import *


class IPGJOA:

    def __init__(self, total_nodes):
        self.total_nodes = total_nodes
        self.population_size = POPULATION_SIZE
        self.num_cluster_heads = NUM_CLUSTER_HEADS
        self.population = []

    def initialize_population(self):
        """
        Generate random candidate Cluster Head solutions.
        """

        self.population = []

        for i in range(self.population_size):

            candidate = random.sample(
                range(self.total_nodes),
                self.num_cluster_heads
            )

            candidate.sort()

            self.population.append(candidate)

        return self.population

    def display_population(self):

        print("\n========== Initial Population ==========\n")

        for i, solution in enumerate(self.population):
            print(f"Solution {i+1:2d} : {solution}")

        print("\n========================================")

    def hunting_energy(self, iteration):
        L1 = 1

        M = (
            0.05
            * L1
            * math.exp(
                -2 * ((iteration / MAX_ITERATIONS) ** 2)
            )
        )

        return M 
       
    def select_male_female_jackals(self, fitness_values):
        """
        Select the best (Male) and second-best (Female)
        solutions based on fitness.
        """

        ranked = list(zip(self.population, fitness_values))

        ranked.sort(
            key=lambda x: x[1],
            reverse=True
        )

        male = ranked[0]
        female = ranked[1]

        return male, female