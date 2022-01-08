# This question is asked by Google. Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list.

# Ex: Given the following linked lists and values...

# 1->2->3->null, value = 3, return 1->2->null
# 8->1->1->4->12->null, value = 1, return 8->4->12->null
# 7->12->2->9->null, value = 7, return 12->2->9->null
# Thanks,
# The Daily Byte
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next