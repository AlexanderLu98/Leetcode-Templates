from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLists:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
    
    def mergeTwoListsRecursive(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1
        l2.next = self.mergeTwoListsRecursive(l1, l2.next)
        return l2

if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(4)))
    head2 = ListNode(1, ListNode(3, ListNode(4)))
    s = MergeLists()
    print(s.mergeTwoLists(head1, head2))
    print(s.mergeTwoListsRecursive(head1, head2))