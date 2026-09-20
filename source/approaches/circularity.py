'''
Implements the Rotate List problem using the Circularity approach. 🔄⭕

The approach identifies the new tail and new head based on the effective rotation count, 
temporarily reconnects the original list around the rotation boundary, 
and restores the final linear structure by linking the original tail to the original head.

    - 📏 Calculates the list length and reduces k using modulo.
    - 🎯 Locates the new head and new tail directly.
    - ✂️ Breaks the list at the rotation boundary.
    - 🔗 Connects the original tail to the original head.
    - 💾 Performs all modifications in-place with O(1) auxiliary space.
'''
from listnode import ListNode
from typing import Optional

class Circularity:
    def __init__(self, head: Optional[ListNode], k: int) -> None:
        self.head: Optional[ListNode] = head
        self.k: int = k

    def rotate(self) -> Optional[ListNode]:
        # 🛑 Empty or single-node lists need no rotation.
        if not self.head or not self.head.next:
            return self.head

        def getLength(current_node: Optional[ListNode]) -> int:
            # 📏 Count the total number of nodes in the list.
            list_length: int = 0

            while current_node:
                list_length += 1
                current_node = current_node.next

            return list_length

        # 📏 Reduce k to the effective number of rotations.
        list_length: int = getLength(self.head)
        self.k %= list_length

        # 🛑 A full-length rotation leaves the list unchanged.
        if self.k == 0:
            return self.head

        # ✂️ Find the node that will become the new tail.
        new_tail: Optional[ListNode] = self.head

        for _ in range(list_length - self.k - 1):
            new_tail = new_tail.next

        # 🎯 The node after the new tail becomes the new head.
        new_head: Optional[ListNode] = new_tail.next

        # ✂️ Break the list at the new tail.
        new_tail.next = None

        # 🔗 Connect the old tail to the original head.
        old_tail: Optional[ListNode] = new_head

        while old_tail.next:
            old_tail = old_tail.next

        old_tail.next = self.head

        return new_head
