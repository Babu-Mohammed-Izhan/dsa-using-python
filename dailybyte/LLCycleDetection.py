# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


#! Problem uses the turtle and hare solution
#! walker goes only 1 step
#! runner goes only 2 steps
#! When runner == walker then theres a cycle
#! When runner != walker then theres no cycle



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker = runner = head
        
        while runner != None and runner.next != None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        
        return False


#! Problem uses the turtle and hare solution
#! walker goes only 1 step
#! runner goes only 2 steps
#! When runner == walker then theres a cycle
#! When runner != walker then theres no cycle
#! If there is a cycle find the start node
#! To find the start node use walker and runner at the same pace
#! If both are equal then, its the start node

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker = runner = head
        isCycle = False
        
        while runner != None and runner.next != None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                isCycle = True
                break
        
        if not isCycle:
            return None
        walker = head
        while walker != runner:
            walker = walker.next
            runner = runner.next
        return walker

