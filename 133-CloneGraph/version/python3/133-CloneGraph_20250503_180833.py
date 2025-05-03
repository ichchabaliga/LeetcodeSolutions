# Last updated: 03/05/2025, 18:08:33
# recursively build the graph by adding the node to the visited set
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node in self.visited:
            copy=self.visited[node]
        else:
            copy=Node(node.val)
            self.visited[node] = copy
        for n in node.neighbors:
            if n in self.visited:
                copy.neighbors.append(self.visited[n])
            else:
                copy.neighbors.append(self.cloneGraph(n))
        return copy
