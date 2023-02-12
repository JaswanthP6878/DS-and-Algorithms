'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
'''



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None} ## to map the old list nodes to new list nodes
        # here None is mapped because curr.random / curr.next can get None values so we have to handle
        # this case.
        curr = head
        while curr:
            New = Node(curr.val) #create a new carbon copy node
            mp[curr] = New  # map the old node to new Node
            curr = curr.next

        curr = head
        while curr:
            New = mp[curr] # get the new Node
            New.next = mp[curr.next] #assignthe next pointer of new node to be same as next pointer of old Node 
            New.random = mp[curr.random] #assignthe next pointer of new node to be same as next pointer of old Node 
            curr = curr.next

        return mp[head] # return the new Node corresponding to the head of old node
