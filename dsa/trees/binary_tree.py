"""Binary Tree."""


class Node:
    """Binary Tree Node."""

    def __init__(self, data: int) -> None:
        """Instantiate Node object."""
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        """String representation of node object."""
        return str(self.data)


class BinaryTree:
    """Binary Tree."""

    def __init__(self) -> None:
        """Instantiate Binary Tree object."""
        self.root = None
        self.inorder_print_queue = list()
        self.level_order_print_queue = list()

    def insert(self, root: Node, data: int):
        """Insert the given data into tree."""

        if root is None:
            self.root = Node(data=data)
            return

        queue = list()
        queue.append(root)

        while len(queue) > 0:
            # Traverse the node and find appropriate location for the data to be inserted. Once inserted, simply return.

            temp_node = queue.pop(0)
            if temp_node.left is not None:
                queue.append(temp_node.left)
            else:
                temp_node.left = Node(data=data)
                return
            if temp_node.right is not None:
                queue.append(temp_node.right)
            else:
                temp_node.right = Node(data=data)
                return

    def delete(self, data: int):
        """Delete the given data/node from the tree.
        Note: Deletion is different from deletion in BST. Here the deleted node is replaced with deepest right most node.
        """

        if self.root is None:
            return

        queue = [self.root]
        node_to_replace = None

        while len(queue) > 0:
            node = queue.pop(0)

            if node.data == data:
                node_to_replace = node

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        if node_to_replace is not None:
            # Replacing the value of the node to be deleted with value from the deepest right most node.

            node_to_replace.data = node.data

            # Deleting the deepest right most node.
            queue = [self.root]
            while len(queue) > 0:
                temp_node = queue.pop(0)

                # node refers to the last node we had from the while loop above.
                if temp_node is node:
                    node = None
                    return

                if temp_node.left is not None:
                    if temp_node.left is node:
                        temp_node.left = None
                    else:
                        queue.append(temp_node.left)
                if temp_node.right is not None:
                    if temp_node.right is node:
                        temp_node.right = None
                    else:
                        queue.append(temp_node.right)

    def print_inorder(self, node: Node):
        """Display tree and it's content in inorder fashion."""

        if node is not None:
            self.print_inorder(node=node.left)
            print(node.data, end=" ")
            self.print_inorder(node=node.right)

    def print_level_order(self):
        """Level order traversal."""

        if self.root is None:
            return
        queue = [self.root]

        while len(queue) > 0:
            node_to_print = queue.pop(0)
            print(node_to_print.data, end=" ")

            if node_to_print.left is not None:
                queue.append(node_to_print.left)

            if node_to_print.right is not None:
                queue.append(node_to_print.right)


if __name__ == "__main__":
    """Driver code."""

    array = [10, 20, 30, 40, 50, 60, 70, 80]
    tree = BinaryTree()
    root = tree.root

    for i in array:
        tree.insert(root=tree.root, data=i)

    print("Inorder Traversal.")
    tree.print_inorder(node=tree.root)
    print("\n")

    print("Level Order Traversal.")
    tree.print_level_order()
    print("\n")

    print("Deleting a node -> 20")
    tree.delete(data=20)
    print("\n")

    print("Level Order Traversal.")
    tree.print_level_order()
    print("\n")
