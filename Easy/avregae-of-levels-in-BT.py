from typing import List
import numpy as np


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        val_arr = []
        while queue:
            node = queue.pop(0)
            val_arr.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result = [[val_arr[0]]]
        idx = 1
        while idx <= len(val_arr):
            old_idx = idx
            idx = 2 * idx + 1
            result.append([val_arr[old_idx:idx]])
        return [np.mean(result[arr]) for arr in result]
