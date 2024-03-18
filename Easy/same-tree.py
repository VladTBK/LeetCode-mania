from typing import Optional, Any


class TreeNode:
    def __init__(self, val: int = 0, left: Any = None, right: Any = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def anyDFS(self, root: Optional[TreeNode], arr: list[Any]) -> None:
        if not root:
            return
        self.anyDFS(root.left)  # type:ignore
        arr.append(root.val)
        self.anyDFS(root.right)  # type:ignore

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first_arr: list[Any] = []
        second_arr: list[Any] = []
        self.anyDFS(p, first_arr)
        self.anyDFS(q, second_arr)
        return first_arr == second_arr
