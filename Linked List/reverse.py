from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Helper function for generators
def stitch(*nodes):
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
    
#Helper function for generators
def node_iter(node):
    while node:
        yield node
        node = node.next

#Helper function for printing the list
def print_list(node: Optional[ListNode]):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print(result)

class ReverseList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p
    
    # sol 1 using stack

    def reverseListGenerators(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        for node in node_iter(head):
            stack.append(node)

        dummy = ListNode()
        cur = dummy
        while stack:
            node = stack.pop()
            stitch(cur, node)
            cur = cur.next

        cur.next = None

        return dummy.next
    
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = ReverseList()
    reversed_list = s.reverseList(head)
    print_list(reversed_list)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_list_recursive = s.reverseListRecursive(head)
    print_list(reversed_list_recursive)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_list_generators = s.reverseListGenerators(head)
    print_list(reversed_list_generators)