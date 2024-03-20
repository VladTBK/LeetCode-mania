# Definition for a binary tree node.
from typing import List, Any


class TreeNode:
    def __init__(self, val: int = 0, left: Any = None, right: Any = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def parse_arr(self, arr) -> str:
        output = ""
        for val in arr:
            output += str(val) + "->"
        return output[:-2]

    def dfs_parsing(self, root: TreeNode, arr: List[int]) -> None:
        if not root:
            return None

        self.dfs_parsing(root.left, arr)
        arr.append(root.val)
        self.dfs_parsing(root.right, arr)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        nodes_arr: List[int] = []
        root_val = root.val
        root_idx = -1
        self.dfs_parsing(root, nodes_arr)

        for i in range(len(nodes_arr)):
            if nodes_arr[i] == root_val:
                root_idx = i
                break
        first_arr = nodes_arr[:root_idx]
        second_arr = nodes_arr[root_idx + 1 :]
        if first_arr:
            first_arr = [1] + first_arr
            first_arr = first_arr[::-1]
        if second_arr:
            second_arr = [1] + second_arr
        return [self.parse_arr(first_arr), self.parse_arr(second_arr)]
