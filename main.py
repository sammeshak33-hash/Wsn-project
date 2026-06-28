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
    # Hunting Energy
    # ----------------------------
    print("\n========== Hunting Energy ==========\n")

    for iteration in range(1, 6):

        M = optimizer.hunting_energy(iteration)

        print(f"Iteration {iteration}")
        print("Searching Energy :", round(M, 6))
        print("--------------------------------") 

if __name__ == "__main__":
    main()