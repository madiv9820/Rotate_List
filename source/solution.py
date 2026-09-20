'''
Implements the Rotate List solution using an in-place Reverse → Split → Reverse strategy. 🔄🔗

The implementation first calculates the effective rotation count, reverses the entire linked list, splits it after the first k nodes, reverses both resulting portions, and finally reconnects them to produce the rotated list.

    - 📏 Calculates the list length to reduce unnecessary rotations.
    - 🔄 Reverses linked-list portions in-place.
    - ✂️ Splits the reversed list at the rotation boundary.
    - 🔗 Reconnects the two portions to form the rotated list.
    - 💾 Uses O(1) auxiliary space.
'''
from listnode import ListNode
from typing import Optional
from .approaches import Reversal, Circularity

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reversal: Reversal = Reversal(head, k)
        circularity: Circularity = Circularity(head, k)
        return reversal.rotate()
    