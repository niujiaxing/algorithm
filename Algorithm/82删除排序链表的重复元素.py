# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummynode = ListNode(-1)
        dummynode.next = head
        if not head:
            return head
        cur = dummynode
        curval = head.val
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
  
        return dummynode.next
# 时间复杂度：O(n)
# 空间复杂度：O(1)