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