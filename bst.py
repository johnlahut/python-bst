"""
BST implementation in Python

Implementation includes functionality to add nodes, print the tree, and search for a node
This program is largely based off of the algorithm defined in Cormen et. al, page 294
The program tends to opt for iterative versions for each of the methods as per Cormen, they
are more efficient.

:author: John Lahut
:class: CSI 503

"""

class Node:
    """
    Represents a node within a Tree
    """

    def __init__(self, value: int):
        """
        Initializes a Node object with the given value
        :param value: value for the Node object to contain
        """

        self.left = None
        self.right = None
        self.value = value
        self.parent = None

    def __str__(self):
        return f'value: {self.value}'


class Tree:

    def __init__(self):
        """
        Initializes a Tree object with no root
        """
        self.root = None

    def insert(self, value: int):
        """
        Inserts a value into the BST

        :param value: value to be inserted into the BST
        :return: None
        """

        x = self.root
        y = None
        z = Node(value)

        # find where on the tree this value should go
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y

        # tree is empty
        if y is None:
            self.root = z

        # value goes on left leaf
        elif z.value < y.value:
            y.left = z

        # value goes on right leaf
        else:
            y.right = z

    def max(self, x: Node = None) -> Node:
        """
        Returns a pointer to the maximum value of the BST
        :param x: Takes the root of the subtree to find the max, otherwise its the root
        :return:
        """

        if not x:
            x = self.root

        # we know the max value is always to the right
        while x.right is not None:
            x = x.right
        return x

    def min(self, x: Node = None) -> Node:
        """
        Returns a pointer to the minimum value of the BST

        :param x: Takes the root of the subtree to find the min, otherwise its the root
        :return: Pointer to maximum value of the tree
        """

        if not x:
            x = self.root


        # we know the max value is always to the right
        while x.left is not None:
            x = x.left
        return x


    def search(self, value: int) -> Node:
        """
        Searches for the value in the BST
        :param value: value to search for
        :return: None if not found, otherwise Node object where the value was found
        """
        x = self.root

        # keep branching until we find the value, or return none
        while x is not None and x.value != value:
            if value < x.value:
                x = x.left
            else:
                x = x.right
        return x



    def print(self, node: Node):
        """
        Prints the tree, effectively performing in-order traversal
        :param node: Starting point to start the traversal
        :return: None
        """

        if node is None:
            return
        self.print(node.left)
        print(node.value)
        self.print(node.right)

    def _transplant(self, parent: Node, child: Node):
        """
        Essentially swaps the child and parent nodes around.
        To be used as a private method to delete

        :param parent: Parent node to swap
        :param child: Child node to swap
        :return: None
        """

        if parent.parent is None:
            self.root = child
        elif parent == parent.parent.left:
            parent.parent.left = child
        else:
            parent.parent.right = child
        if child is not None:
            child.parent = parent.parent

    def delete(self, node: Node):
        """
        Deletes a node from the BST

        :param node: node to delete from the tree
        :return: None
        """

        if node.left == None:
            self._transplant(node, node.right)
        elif node.right == None:
            self._transplant(node, node.left)
        else:
            min = self.min(node.right)
            if min.parent != node:
                self._transplant(min, min.right)
                min.right = node.right
                min.right.parent = min
            self._transplant(node, min)
            min.left = node.left
            min.left.parent = min

    def successor(self, node: Node) -> Node:
        """
        Finds the successor of the given node. i.e. the smallest key
        greater than the node's key

        :param node: the node to find the successor of
        :return: The node's successor
        """

        if node.right is not None:
            return self.min(node.right)
        temp = node.parent
        while temp is not None and node == temp.right:
            node = temp
            temp = node.parent
        return temp

    def predecessor(self, node: Node) -> Node:
        """
        Finds the predecessor of the given node

        :param node: the node to find the predecessor of
        :return: The node's predecessor
        """
        if node.left is not None:
            return self.max(node.left)
        temp = node.parent
        while temp is not None and node == temp.left:
            node = temp
            temp = node.parent
        return temp
