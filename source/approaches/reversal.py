'''
Implements the Rotate List problem using the Reversal approach. 🔄🔗

The approach reverses the entire linked list, splits it at the effective rotation boundary, 
reverses both resulting portions, and reconnects them to produce the rotated list.

    - 📏 Calculates the list length and reduces k using modulo.
    - 🔄 Reverses the complete linked list in-place.
    - ✂️ Splits the reversed list after the first k nodes.
    - 🔄 Reverses both portions to restore their correct order.
    - 🔗 Connects the two portions to form the rotated list.
    - 💾 Uses O(1) auxiliary space.
'''
from listnode import ListNode
from typing import Optional

class Reversal:
    def __init__(self, head: Optional[ListNode], k: int) -> None:
        self.head: Optional[ListNode] = head
        self.k: int = k

    def rotate(self) -> Optional[ListNode]:
        # 🛑 Empty, single-node, or already complete list needs no rotation.
        if not self.head or not self.head.next:
            return self.head

        def getLength(current_node: Optional[ListNode]) -> int:
            # 📏 Traverse the list to calculate its total number of nodes.
            list_length: int = 0

            while current_node:
                list_length += 1
                current_node = current_node.next

            return list_length

        def reverseList(current_node: Optional[ListNode]) -> Optional[ListNode]:
            # 🔄 Reverse the list in-place by rewiring each next pointer.
            previous_node: Optional[ListNode] = None

            while current_node:
                next_node: Optional[ListNode] = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            return previous_node

        # 📏 Find the list length and reduce k to effective rotations.
        list_length: int = getLength(self.head)
        self.k %= list_length

        # 🛑 Rotating by the list length leaves the list unchanged.
        if self.k == 0:
            return self.head

        # 🔄 Reverse the complete list.
        reversed_head: Optional[ListNode] = reverseList(self.head)

        # ✂️ Locate the split point after the first k nodes.
        split_node: Optional[ListNode] = reversed_head

        for _ in range(self.k - 1):
            split_node = split_node.next

        # 🔀 Separate the two reversed portions.
        second_part_head: Optional[ListNode] = split_node.next
        split_node.next = None

        # 🔄 Reverse both portions to restore their original order.
        first_part_head: Optional[ListNode] = reverseList(reversed_head)
        second_part_head = reverseList(second_part_head)

        # 🔗 Connect the first portion with the rotated second portion.
        first_part_tail: Optional[ListNode] = first_part_head

        while first_part_tail.next:
            first_part_tail = first_part_tail.next

        first_part_tail.next = second_part_head

        return first_part_head
        