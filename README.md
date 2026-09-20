# [🔄 The Linked List Carousel — Rotate, Reconnect & Roll! 🎠🔗](https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150)

### 📖 A Little Story

Imagine a queue of people standing in a circle. Instead of everyone moving one step at a time, we simply decide **where the new line should begin** and reconnect the remaining people around it. 😄🔗

That is exactly what we do here: rotate the linked list to the right by **`k`** places by finding the correct new head and rearranging the links.

### 📝 Problem

Given the **`head`** of a linked list, rotate the list to the **right by `k` places** and return the new head.

For example:

```text
1 → 2 → 3 → 4 → 5
```

Rotating it right by **`2`** places moves the last two nodes to the front:

```text
4 → 5 → 1 → 2 → 3
```

#### 🧪 Examples

- **🧪 Example 1 — Two-Step Rotation**

    ![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)
    
    ```text
    Input:  head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
    ```

    The last **`2`** nodes move to the beginning. 🔄

- **🧪 Example 2 — Rotation Beyond List Length**

    ![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

    ```text
    Input:  head = [0,1,2], k = 4
    Output: [2,0,1]
    ```

    Since the list contains only **`3`** nodes, rotating **`4`** times is equivalent to rotating:

    ```text
    4 % 3 = 1
    ```

    So the list moves right by only one position. ♻️

#### 📌 Constraints

* **`0 ≤ number of nodes ≤ 500`**
* **`-100 ≤ Node.val ≤ 100`**
* **`0 ≤ k ≤ 2 × 10⁹`**

---

### 🧭 Approaches

Rotating a linked list can be achieved by either **rearranging nodes through reversals** or by directly **rewiring the list around its rotation boundary**. Both approaches run in linear time and use constant extra space, but their pointer operations differ. 🔗

- #### 🔄 Reversal

    Instead of moving nodes one by one, we can rearrange the list using **three reversals**. The key is that after reversing the complete list, the last **`k`** nodes appear at the beginning, making the rotation boundary easy to identify. 🔗

    - **🧠 Intuition**

        For:

        ```text
        1 → 2 → 3 → 4 → 5    k = 2
        ```

        Reverse everything:

        ```text
        5 → 4 → 3 → 2 → 1
        ```

        Split after `k` nodes:

        ```text
        5 → 4 | 3 → 2 → 1
        ```

        Reverse both parts:

        ```text
        4 → 5 | 1 → 2 → 3
        ```

        Connect them to obtain the rotated list. 🎯

    - **🪜 Steps**

        1. 📏 Find the list length and calculate **`k % length`**.
        2. 🛑 Return the original list if **`k == 0`**.
        3. 🔄 Reverse the complete list.
        4. ✂️ Split it after the first **`k`** nodes.
        5. 🔄 Reverse both resulting portions.
        6. 🔗 Connect the two portions.
        7. 🎯 Return the new head.

    - **🧾 Pseudocode**

        ```text
        length = getLength(head)
        k = k % length

        if k == 0:
            return head

        head = reverse(head)

        split_node = node after first k nodes
        second_part = split_node.next
        split_node.next = null

        first_part = reverse(head)
        second_part = reverse(second_part)

        connect first_part → second_part

        return first_part
        ```

    - **⏱️ Complexity**

        * **Time:** **`O(n)`** — the list is traversed a constant number of times.
        * **Space:** **`O(1)`** — all operations are performed in-place.

- #### ⭕ Circularity

    A rotation naturally suggests a **circle**: connect the last node back to the first, walk to the point where the new list should begin, and break the circle there. 🔗⭕ This avoids reversing any nodes.

    - **🧠 Intuition**

        For:

        ```text
        1 → 2 → 3 → 4 → 5    k = 2
        ```

        The new head should be **`4`**, and the new tail should be **`3`**:

        ```text
        1 → 2 → 3 | 4 → 5
                ↑     ↓
                └─────┘
        ```

        Once the connection is made, breaking it at **`3`** produces:

        ```text
        4 → 5 → 1 → 2 → 3
        ```

    - **🪜 Steps**

        1. 📏 Find the list length and calculate **`k % length`**.
        2. 🛑 Return the original list if **`k == 0`**.
        3. 🎯 Find the new tail at position **`length - k`**.
        4. 🔗 Connect the original tail to the original head.
        5. ✂️ Break the link after the new tail.
        6. 🎯 Return the new head.

    - **🧾 Pseudocode**

        ```text
        length = getLength(head)
        k = k % length

        if k == 0:
            return head

        new_tail = node at position length - k
        new_head = new_tail.next

        find old_tail
        old_tail.next = head

        new_tail.next = null

        return new_head
        ```

    - **⏱️ Complexity**

        * **Time:** **`O(n)`** — the list is traversed a constant number of times.
        * **Space:** **`O(1)`** — only a few pointers are used.



| Approach          | Core Idea                                                  |   Time |  Space | Key Operations             |
| ----------------- | ---------------------------------------------------------- | -----: | -----: | -------------------------- |
| 🔄 **Reversal**   | Reverse, split, reverse again, then reconnect              | **`O(n)`** | **`O(1)`** | Multiple reversals + split |
| ⭕ **Circularity** | Connect the ends, locate the new tail, then break the link | **`O(n)`** | **`O(1)`** | Rewire + split             |

**💡 Key Difference** 
- **Reversal** transforms the list to make the rotation boundary easier to construct.
- **Circularity** works directly with the rotation boundary and requires fewer pointer transformations. 🔗✂️

---