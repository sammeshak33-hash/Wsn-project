from deployment import deploy_nodes, plot_deployment
from neighbor_discovery import discover_neighbors
from energy_model import (
    transmit_packet,
    receive_packet,
    print_energy,
)
from config import PACKET_SIZE

from ip_gjoa import IPGJOA

from fitness import FitnessCalculator

from cluster_formation import ClusterFormation

from trust_computation import TrustComputation

def main():

    # ----------------------------
    # Deploy Nodes
    # ----------------------------
    nodes = deploy_nodes()

    # ----------------------------
    # Discover Neighbors
    # ----------------------------
    nodes = discover_neighbors(nodes)

    # ----------------------------
    # Plot Deployment
    # ----------------------------
    plot_deployment(nodes)

    # ----------------------------
    # Display first 10 nodes
    # ----------------------------
    print("\nNode Information\n")

    for node in nodes[:10]:
        print(f"Node {node.id}")
        print(f"Location : ({node.x:.2f}, {node.y:.2f})")
        print(f"Distance to BS : {node.distance_to_bs:.2f}")
        print(f"Neighbors : {node.neighbors}")
        print("-" * 40)

    # ----------------------------
    # Energy Model Test
    # ----------------------------
    print("\n==============================")
    print("ENERGY MODEL TEST")
    print("==============================")

    sender = nodes[0]
    receiver = nodes[1]

    distance = 20  # meters

    print("\nBefore Transmission")
    print_energy(sender)
    print_energy(receiver)

    tx_energy = transmit_packet(sender, PACKET_SIZE, distance)
    rx_energy = receive_packet(receiver, PACKET_SIZE)

    print("\nTransmission Completed")
    print(f"Transmission Energy : {tx_energy:.12f} J")
    print(f"Reception Energy    : {rx_energy:.12f} J")

    print("\nAfter Transmission")
    print_energy(sender)
    print_energy(receiver)


    # ----------------------------
    # Ip-GJOA Initialization
    # ----------------------------
    print("\n==============================")
    print("IP-GJOA INITIALIZATION")
    print("==============================")

    optimizer = IPGJOA(len(nodes))

    optimizer.initialize_population()

    optimizer.display_population()

    # ----------------------------
    # Fitness Evaluation
    # ----------------------------
    fitness = FitnessCalculator(nodes)

    print("\n========== Fitness Evaluation ==========\n")

    for i, solution in enumerate(optimizer.population):

        fitness_value = fitness.calculate_fitness(solution)

        print(f"Solution {i+1}")
        print("Cluster Heads :", solution)
        print("Fitness :", round(fitness_value, 6))
        print("---------------------------------------")
    # ----------------------------
    # Elite Jackal Selection
    # ----------------------------
    fitness_values = []

    for solution in optimizer.population:
        fitness_values.append(
            fitness.calculate_fitness(solution)
        )

    male, female = optimizer.select_male_female_jackals(
        fitness_values
    )

    print("\n========== Elite Jackals ==========\n")

    print("Male Jackal")
    print("Solution :", male[0])
    print("Fitness :", round(male[1], 6))
    print()

    print("Female Jackal")
    print("Solution :", female[0])
    print("Fitness :", round(female[1], 6))

    # ----------------------------
    # Position Update Test
    # ----------------------------
    print("\n========== Position Update ==========\n")

    current_solution = optimizer.population[2]

    print("Current Solution :", current_solution)
    print("Male Solution    :", male[0])
    print("Female Solution  :", female[0])

    new_solution = optimizer.update_position(
        current_solution,
        male[0],
        female[0]
    )

    print("\nUpdated Solution :", new_solution)

    # ----------------------------
    # Exploration Phase
    # ----------------------------
    print("\n========== Exploration Phase ==========\n")

    explored_solution = optimizer.exploration_phase(
        new_solution
    )

    print("Before Exploration")
    print(new_solution)

    print()

    print("After Exploration")
    print(explored_solution)   
    # ----------------------------
    # Exploitation Phase
    # ----------------------------
    print("\n========== Exploitation Phase ==========\n")

    exploited_solution = optimizer.exploitation_phase(
        explored_solution
    )

    print("Before Exploitation")
    print(explored_solution)

    print()

    print("After Exploitation")
    print(exploited_solution)

    # ----------------------------
    # Hunting Energy
    # ----------------------------
    print("\n========== Hunting Energy ==========\n")

    for iteration in range(1, 6):

        M = optimizer.hunting_energy(iteration)

        print(f"Iteration {iteration}")
        print("Searching Energy :", round(M, 6))
        print("--------------------------------") 

    print("\n========== Optimization ==========\n")

    best_solution, best_fitness, history = optimizer.optimize(fitness)

    print("\n========== Final Result ==========\n")

    print("Best Cluster Head Solution :")
    print(best_solution)

    print()

    print("Best Fitness :", round(best_fitness, 6))   

    # ----------------------------
    # Cluster Formation
    # ----------------------------

    cluster = ClusterFormation(nodes)

    clusters = cluster.form_clusters(best_solution)

    cluster.display_clusters()  

    # ----------------------------
    # Trust Computation
    # ----------------------------
 
    trust = TrustComputation(nodes)

    trust.initialize_trust()

    # Direct Trust
    trust.calculate_direct_trust()
    trust.display_direct_trust()

    # Indirect Trust
    trust.calculate_indirect_trust()
    trust.display_indirect_trust()


if __name__ == "__main__":
    main()