"""AVL Tree Implementation."""


class AVLNode:
    """AVL Tree Node."""

    def __init__(self, data: int) -> None:
        """Instantiate AVLNode object."""
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        """String representation of node data."""
        return str(self.data)

    @property
    def balance_factor(self) -> int:
        """Get balance factor."""

        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0

        return left_height - right_height


class AVLTree:
    """AVL Tree."""

    def get_height(self, node: AVLNode) -> int:
        """Returns the height of the given node."""

        return node.height if node is not None else 0

    def update_height(self, node: AVLNode) -> int:
        """Updates the height of the node."""

        node.height = 1 + max(
            self.get_height(node=node.left), self.get_height(node=node.right)
        )

    def insert(self, node: AVLNode, data: int):
        """Insert data into the AVL Tree."""

        if node is None:
            return AVLNode(data=data)
        elif data < node.data:
            node.left = self.insert(node=node.left, data=data)
        elif data > node.data:
            node.right = self.insert(node=node.right, data=data)

        self.update_height(node=node)
        balance_factor = node.balance_factor

        # Heavier on the left side
        if balance_factor > 1:
            if data < node.left.data:
                # Left-Left
                return self.right_rotate(node=node)
            elif data > node.left.data:
                # Left-Right
                node.left = self.left_rotate(node=node.left)
                return self.right_rotate(node=node)

        # Heavier on the right side
        if balance_factor < -1:
            if data > node.right.data:
                # Right-Right
                return self.left_rotate(node=node)
            elif data < node.right.data:
                # Right-Left
                node.right = self.right_rotate(node=node.right)
                return self.left_rotate(node=node)

        return node

    def left_rotate(self, node: AVLNode):
        """Perform left rotation."""

        # Set node's right as the new root
        new_root = node.right

        # Set new root's left as node's right
        node.right = new_root.left

        # Set the node as the left of the new root
        new_root.left = node

        self.update_height(node=node)
        self.update_height(node=new_root)

        return new_root

    def right_rotate(self, node: AVLNode):
        """Perform right rotation."""

        # Set node's left as new root
        new_root = node.left

        # Set new root's right as current node's left
        node.left = new_root.right

        # Set node as the right of the new root
        new_root.right = node

        self.update_height(node=node)
        self.update_height(node=new_root)

        return new_root

    def print_level_order(self, node: AVLNode):
        """Level order traversal."""

        if node is None:
            return
        queue = [node]

        while len(queue) > 0:
            node_to_print = queue.pop(0)
            print(node_to_print.data, end=" ")

            if node_to_print.left is not None:
                queue.append(node_to_print.left)

            if node_to_print.right is not None:
                queue.append(node_to_print.right)


if __name__ == "__main__":
    array = [40, 20, 10, 25, 30, 22, 50]
    tree = AVLTree()
    root = None
    for item in array:
        root = tree.insert(node=root, data=item)

    print("Level Order Traversal")
    tree.print_level_order(node=root)
    print("\n")
