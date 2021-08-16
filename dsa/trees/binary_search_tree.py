"""Binary Tree."""

from hashlib import new
from random import randint
from typing import List


class BSTNode:
    """Binary Search Tree Node."""

    def __init__(self, data: int) -> None:
        """Instantiate a binary search tree node object."""
        self.data = data
        self.left = None
        self.right = None

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self) -> str:
        """String representation of binary search tree node object."""
        return str(self.data)


class BinarySearchTree:
    """Binary Search Tree."""

    def __init__(self) -> None:
        """Instantiate binary tree object."""
        self.root = None

    def insert(self, node: BSTNode, data: int):
        """Insert given data into binary tree."""

        if data < node.data:
            if node.left is not None:
                return self.insert(node=node.left, data=data)
            else:
                node.left = BSTNode(data=data)
        if data > node.data:
            if node.right is not None:
                return self.insert(node=node.right, data=data)
            else:
                node.right = BSTNode(data=data)

    def print_preorder(self, node: BSTNode):
        """Display tree and it's content in preorder fashion."""
        if node is not None:
            print(node.data, end=" ")
            self.print_preorder(node=node.left)
            self.print_preorder(node=node.right)

    def print_inorder(self, node: BSTNode):
        """Display tree and it's content in inorder fashion."""

        if node is not None:
            self.print_inorder(node=node.left)
            print(node.data, end=" ")
            self.print_inorder(node=node.right)

    def print_postorder(self, node: BSTNode):
        """Display tree and it's content in postorder fashion."""

        if node is not None:
            self.print_postorder(node=node.right)
            self.print_postorder(node=node.left)
            print(node.data, end=" ")

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

    def search(self, data: int):
        """Search data in the tree."""

        node = self.root
        level = 0

        while node is not None:

            if data == node.data:
                print(f"{data} found at level {level}")
                return

            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right

            level += 1

        if node is None:
            print(f"{data} is not in tree")

    def delete(self, node: BSTNode, data: int):
        """Delete the given node from the tree."""

        # Return None when either we send an empty tree or the given node is not present in the tree
        if node is None:
            return node

        if data > node.data:
            node.right = self.delete(node=node.right, data=data)

        elif data < node.data:
            node.left = self.delete(node=node.left, data=data)

        else:
            # Case:1 -> If the node to be deleted is leaf
            if node.is_leaf:
                node = None
                return None

            # Case:2 -> Node has right child
            elif node.left is None:
                temp = node.right
                node = None
                return temp

            # Case:3 -> Node has left child
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Case:4 -> Node has both left and right. Find min value in right subtree and replace node value with the min value.
            else:

                temp = node.right

                while temp.left is not None:
                    temp = temp.left

                node.data = temp.data
                node.right = self.delete(node=node.right, data=temp.data)

        return node


if __name__ == "__main__":
    """Driver code."""
    tree = BinarySearchTree()

    for i in [84, 99, 62, 74, 31, 88, 81, 41, 27]:
        if tree.root is None:
            tree.root = BSTNode(data=i)
        else:
            tree.insert(node=tree.root, data=i)

    print("Preorder Traversal")
    tree.print_preorder(node=tree.root)
    print("\n")

    print("Inorder Traversal")
    tree.print_inorder(node=tree.root)
    print("\n")

    print("Postorder Traversal")
    tree.print_postorder(node=tree.root)
    print("\n")

    print("Level Order Traversal")
    tree.print_level_order()
    print("\n")

    print("Searching 27")
    tree.search(data=27)
    print("\n")

    print("Searching 99")
    tree.search(data=99)
    print("\n")

    print("Deleting 31")
    tree.root = tree.delete(node=tree.root, data=31)
    print("Deleted 31")
    print("\n")

    print("Inorder Traversal")
    tree.print_inorder(node=tree.root)
    print("\n")
