'''
Defines the reusable ListNode class for representing nodes in a singly linked list. 🔗
'''
from typing import Optional

class ListNode:
    """ 
    🔗 Represents a single node in a singly linked list. 
    
    Each node stores an integer value and a reference 
    to the next node in the chain. 
    """

    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        # 📦 Store the value held by this node.
        self.val: int = val

        # 🔗 Point to the next node, or None at the end of the list.
        self.next: Optional[ListNode] = next

