import random


class TrustComputation:

    def __init__(self, nodes):
        self.nodes = nodes

    def initialize_trust(self):
        """
        Initialize trust values for every node.
        """

        for node in self.nodes:

            node.direct_trust = 1.0
            node.indirect_trust = 1.0
            node.total_trust = 1.0

    def calculate_direct_trust(self):
        """
        Calculate Direct Trust using packet forwarding ratio.
        """

        for node in self.nodes:

            packets_sent = random.randint(80, 100)

            packets_forwarded = random.randint(
                60,
                packets_sent
            )

            node.direct_trust = (
                packets_forwarded /
                packets_sent
            )

    def calculate_indirect_trust(self):

        for node in self.nodes:

            neighbor_trusts = []

            for neighbor_id in node.neighbors:

                neighbor = self.nodes[neighbor_id]

                neighbor_trusts.append(
                    neighbor.direct_trust
                )

            if len(neighbor_trusts) > 0:

                node.indirect_trust = (
                    sum(neighbor_trusts)
                    /
                    len(neighbor_trusts)
                )

            else:

                node.indirect_trust = node.direct_trust 

    def calculate_overall_trust(self):
        """
        Calculate Overall Trust using weighted combination.
        """

        DIRECT_WEIGHT = 0.6
        INDIRECT_WEIGHT = 0.4

        for node in self.nodes:

            node.total_trust = (
                DIRECT_WEIGHT * node.direct_trust
                +
                INDIRECT_WEIGHT * node.indirect_trust
            )                   

    def display_direct_trust(self):
        """
        Display Direct Trust of the first 10 nodes.
        """

        print("\n========== Direct Trust ==========\n")

        for node in self.nodes[:10]:

            print(
                f"Node {node.id:2d} : "
                f"{node.direct_trust:.3f}"
            )

    def display_indirect_trust(self):
        """
        Display Indirect Trust of the first 10 nodes.
        """

        print("\n========== Indirect Trust ==========\n")

        for node in self.nodes[:10]:

            print(
                f"Node {node.id:2d} : "
                f"{node.indirect_trust:.3f}"
            )        

    def display_overall_trust(self):
        """
        Display Overall Trust of the first 10 nodes.
        """

        print("\n========== Overall Trust ==========\n")

        for node in self.nodes[:10]:

            print(
                f"Node {node.id:2d} : "
                f"{node.total_trust:.3f}"
            )        