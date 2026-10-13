# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = sol = ListNode()
        
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if(curr1.val <= curr2.val):
                sol.next = curr1
                curr1 = curr1.next
            else:
                sol.next = curr2
                curr2 = curr2.next
            sol = sol.next
            
        while curr1:
            sol.next = curr1
            curr1 = curr1.next
            sol = sol.next

        while curr2:
            sol.next = curr2
            curr2 = curr2.next
            sol = sol.next

        return ans.next