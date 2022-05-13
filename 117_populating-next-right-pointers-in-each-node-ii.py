"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    def connect(self, root: 'Node') -> 'Node':
        final_dict={}
        def connect_internal(node,level):
            if not node:
                return
            if level not in final_dict:
                final_dict[level]=[]
            final_dict[level].append(node)
            connect_internal(node.left,level+1)
            connect_internal(node.right,level+1)
        connect_internal(root,0)
        for _,given_list in final_dict.items():
            for i in range(len(given_list)-1):
                given_list[i].next=given_list[i+1]
        return root