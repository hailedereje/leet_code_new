# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while(current != None):
            check = False
            while(current.next != None and current.val == current.next.val):
                current, check = current.next, True
            if(check):
                if(prev == None):
                    head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next
        return(head)  