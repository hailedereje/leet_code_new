# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        temp = []
        
        while fast:
            temp.append(fast.val)
            
            if len(temp) == k:
                while temp:
                    slow.val = temp.pop()
                    slow = slow.next
                    
            fast = fast.next
            
        return head