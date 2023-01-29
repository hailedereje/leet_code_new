# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        v = c = 0
        while x.next != None:
            x = x.next
            c+=1
        c = c//2 if c%2 == 0 else c//2 +1
        while(head.next):
            if v == c:
                return head
            head = head.next
            v+=1
        return head
        
        