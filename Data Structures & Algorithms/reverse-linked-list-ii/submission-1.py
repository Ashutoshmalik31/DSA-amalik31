# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        sp = None
        count = 1
        while count < left:
            sp = start
            start = start.next
            count += 1
        
        end = start
        prev = None
        rev_steps = right - left + 1
        while rev_steps > 0:
            nxt = start.next
            start.next = prev
            prev = start
            start = nxt
            rev_steps -= 1
        
        if sp:
            sp.next = prev
        else:
            head = prev
        
        end.next = start
        return head
