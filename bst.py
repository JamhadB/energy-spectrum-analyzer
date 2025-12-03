from node import Node

class BST:
    """
    binary search tree for storing energy values
      - groups duplicate energies using `count`
      - maintains a `subtree_count` for each node
    """

    def __init__(self):
        self.root = None

    def insert(self, energy):
        """
        forces the insert to always start at the root,
        the follows the logic of the helper from there
        """
        self.root = self._insert(self.root, energy)

    def _insert(self, node, energy):
        """
        goes from root node and recursively traverses
        the tree until correct location is found
        """
        if node is None:
            return Node(energy)

        if energy < node.energy:
            # lesser energy, go left
            node.left = self._insert(node.left, energy)
        elif energy > node.energy:
            # greater energy, go right
            node.right = self._insert(node.right, energy)
        else:
            # duplicate val, increase count
            node.count += 1

        # update subtree_count after insert
        # compute number of values in left subtree
        if node.left is not None:
            left_count = node.left.subtree_count
        else:
            left_count = 0

        # compute number of values in right subtree
        if node.right is not None:
            right_count = node.right.subtree_count
        else:
            right_count = 0

        # total number of values in this entire subtree
        node.subtree_count = node.count + left_count + right_count

        return node

    def inorder(self):
        """
        make empty list to store (energy, count) pairs
        starts in-order traversal at the root
        returns sorted list of pairs
        """
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append((node.energy, node.count))
        self._inorder(node.right, result)

    def range_query(self, low, high):
        """
        count how many values in the inclusive range [low, high].
        """
        return self._range_query(self.root, low, high)

    def _range_query(self, node, low, high):
        if node is None:
            return 0

        # node energy too small, right subtree
        if node.energy < low:
            return self._range_query(node.right, low, high)

        # node energy too large, left subtree
        if node.energy > high:
            return self._range_query(node.left, low, high)

        # node in range: include its count + both sides
        return (
            node.count
            + self._range_query(node.left, low, high)
            + self._range_query(node.right, low, high)
        )
