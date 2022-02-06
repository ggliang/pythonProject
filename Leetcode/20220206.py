# 160. Intersection of Two Linked Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head1 = ListNode(2)
head2 = ListNode(2)
p = head2
p.next = ListNode(3)


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None

    pa = headA  # 2 pointers
    pb = headB

    while pa is not pb:
        # if either pointer hits the end, switch head and continue the second traversal,
        # if not hit the end, just move on to next
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next

    return pa


print(getIntersectionNode(head1, head2))
