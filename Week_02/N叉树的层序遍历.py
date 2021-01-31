"""
# Definition for a Node.
class Node(object)
from collections import deque:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []
        if root == None:
            return ans
        deque = collections.deque([root])        
        while deque:
            level = []
            for _ in range(len(deque)):
                node = deque.popleft()
                level.append(node.val)
                deque.extend(node.children)
            ans.append(level)
        return ans

        