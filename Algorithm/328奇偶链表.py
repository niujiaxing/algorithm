class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ## 定义一个偶数节点的头evenhead
        if not head:
            return head
        evenhead = head.next
        odd,even = head,evenhead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
        ## 空间复杂度O（1）
        ## 时间复杂度O（N）