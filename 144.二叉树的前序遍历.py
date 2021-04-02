#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 迭代
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node,TreeNode):
                stack.append(node.right)
                stack.append(node.left)
                stack.append(node.val)
            elif isinstance(node,int):
                res.append(node)
        return res

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     def helper(node):
    #         if node is None:
    #             return 
    #         res.append(node.val)
    #         helper(node.left)
    #         helper(node.right)
    #     helper(root)
    #     return res


        
# @lc code=end

