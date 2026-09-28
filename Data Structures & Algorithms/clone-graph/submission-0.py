"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        st = node
        stack = [st]
        visited = set()
        visited.add(st)
        o_to_n = {}

        while stack:
            pop_node = stack.pop()
            o_to_n[pop_node] = Node(val=pop_node.val)

            for nei in pop_node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        for old_node, new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_neis = o_to_n[nei]
                new_node.neighbors.append(new_neis)
                # append all the neighbors based on the ol;d neighbours
        return o_to_n[st]
        

