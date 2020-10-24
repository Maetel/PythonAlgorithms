# 1_binary_search_tree.py
from typing import List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def is_leaf(self):
        return (not self.left) and (not self.right)


def traverse(node: TreeNode, list: List, order="inorder", append_none: bool = True):
    if not node:
        if append_none:
            list.append(None)
        return
    # if node.is_leaf():
    #    list.append(node.value)
    #    return
    normalized = order.lower()
    if "pre" in normalized:
        list.append(node.value)
        traverse(node.left, list, order)
        traverse(node.right, list, order)
    elif "in" in normalized:
        traverse(node.left, list, order)
        list.append(node.value)
        traverse(node.right, list, order)
    elif "post" in normalized:
        traverse(node.left, list, order)
        traverse(node.right, list, order)
        list.append(node.value)
    return list


def inorder_traverse(node: TreeNode, list: List, append_none=True):
    if not node:
        if append_none:
            list.append(None)
        return

    inorder_traverse(node.left, list)
    list.append(node.value)
    inorder_traverse(node.right, list)


class BinarySearchTree:

    def to_list(self):
        list = []
        traverse(self.root, list)
        return list

    def _add_node_impl(self, node: TreeNode, val):
        if not node:
            return

        if node.value > val:
            if node.left:
                self._add_node_impl(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._add_node_impl(node.right, val)
            else:
                node.right = TreeNode(val)

    def add_node(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return

        self._add_node_impl(self.root, val)

    def __init__(self, list: List = []):
        self.root = None
        if not list:
            return

        for val in list:
            self.add_node(val)


def main():
    #values = [i for i in range(10)]
    values = [7, 20, 5, 15, 10, 4, 4, 33, 2, 25, 6]
    tree = BinarySearchTree(values)
    print(tree.to_list())


if __name__ == '__main__':
    main()
