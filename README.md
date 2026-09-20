# [🔄 The Linked List Carousel — Rotate, Reconnect & Roll! 🎠🔗](https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150)

### 📖 A Little Story

Imagine a queue of people standing in a circle. Instead of everyone moving one step at a time, we simply decide **where the new line should begin** and reconnect the remaining people around it. 😄🔗

That is exactly what we do here: rotate the linked list to the right by `k` places by finding the correct new head and rearranging the links.

### 📝 Problem

Given the `head` of a linked list, rotate the list to the **right by `k` places** and return the new head.

For example:

```text
1 → 2 → 3 → 4 → 5
```

Rotating it right by `2` places moves the last two nodes to the front:

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

    The last `2` nodes move to the beginning. 🔄

- **🧪 Example 2 — Rotation Beyond List Length**

    ![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

    ```text
    Input:  head = [0,1,2], k = 4
    Output: [2,0,1]
    ```

    Since the list contains only `3` nodes, rotating `4` times is equivalent to rotating:

    ```text
    4 % 3 = 1
    ```

    So the list moves right by only one position. ♻️

#### 📌 Constraints

* `0 ≤ number of nodes ≤ 500`
* `-100 ≤ Node.val ≤ 100`
* `0 ≤ k ≤ 2 × 10⁹`

---