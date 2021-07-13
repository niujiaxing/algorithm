class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for i in range(left - 1):
            pre = pre.next

        cur = pre.next
        ## 穿针引线
        ## 保证前后的链表关系
        for i in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
        ## 时间复杂度 O（N）
        ## 空间复杂度O（1）