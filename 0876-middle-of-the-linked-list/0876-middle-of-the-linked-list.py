# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listed = []
        x = head
        v = 0
        while x.next != None:
            listed.append(head.val)
            x = x.next
        val = len(listed)//2 if len(listed)%2 == 0 else len(listed)//2 +1
        
        while(head.next):
            if v == val:
                return head
            head = head.next
            v+=1
        return head
        
        