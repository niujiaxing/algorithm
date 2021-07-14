class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ## 先设一个dummynode
        ## 利用快慢指针
        ## fast 先走n步
        ## fast快走到末尾的时候删除slow的下一个节点
        dummynode = ListNode(-1)
        dummynode.next = head
        fast,slow = dummynode,dummynode
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummynode.next
        ## 时间复杂度O（L）链表的长度
        ## 空间复杂度O（1）