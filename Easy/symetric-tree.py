from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # type:ignore
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def symDFS(self, node: Optional[TreeNode], arr: list[int]) -> None:
        if not node:
            return
        self.symDFS(node.left, arr)
        arr.append(node.val)
        self.symDFS(node.right, arr)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodes_arr: list[int] = []
        self.symDFS(root, nodes_arr)
        leng = len(nodes_arr) // 2
        first_half = nodes_arr[:leng]
        second_half = nodes_arr[leng + 1 :]
        return first_half == second_half[::-1]
