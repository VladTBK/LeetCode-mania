from typing import Any


class TreeNode:
    def __init__(self, val: int = 0, left: Any = None, right: Any = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # Base Case
            return root
        self.invertTree(root.left)  # Call the left substree
        self.invertTree(root.right)  # Call the right substree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root  # Return the root
