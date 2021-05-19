# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #空链表直接返回
        if head is None:
            return head
        pre = head
        cur = head.next
        while cur is not None:
            nxt = cur.next
            if cur.val == pre.val:
                pre.next = cur.next
                cur.next = None
            else:
                pre = cur
            cur = nxt
        return head
