class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ## 归并排序 sort + merge
        ## 截取中间部分将list分成两份
        if head is None or head.next is None:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(cur)
        return self.merge(l1,l2)

    def merge(self,l1,l2):
        ##合并两个有序链表
        dummynode = ListNode(-1)
        cur = dummynode
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2