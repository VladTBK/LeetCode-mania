from typing import Any


class TreeNode:
    def __init__(self, val: int = 0, left: Any = None, right: Any = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder(self, root: TreeNode, arr: list[int | None]) -> None:
        if not root:
            return None
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return 0
        tree_arr: list[int] = []
        self.preorder(root, tree_arr)
        root.left = None
        node = root
        idx = 1
        while idx < len(tree_arr):
            node.right = TreeNode(tree_arr[idx])
            idx += 1
            node = node.right
