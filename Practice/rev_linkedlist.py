class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # Save next node
            curr.next = prev        # Reverse link
            prev = curr             # Move prev forward
            curr = next_node        # Move current forward

        return prev