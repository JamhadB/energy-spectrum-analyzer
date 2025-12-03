class Node:
    """
    node in the binary search tree

    energy, either float or int,
    is the stored energy value.

    count is how many times
    this exact energy has been inserted

    subtree_count is the total
    number of values stored in this node's
    subtree (including this node's own count)

    left, either Node or None, is the left child
    (energies < this node's energy)

    right is the right child
    (energies > this node's energy)
    """
    def __init__(self, energy):
        self.energy = energy
        self.count = 1

        self.left = None
        self.right = None

        # start with just this node's count
        self.subtree_count = 1
