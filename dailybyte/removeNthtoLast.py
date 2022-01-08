# Good morning,

# Need help with yesterday's problem? Start getting solutions.

# Today's Byte

# This question is asked by Facebook. Given a linked list and a value n, remove the nth to last node and return the resulting list.

# Ex: Given the following linked lists...

# 1->2->3->null, n = 1, return 1->2->null
# 1->2->3->null, n = 2, return 1->3->null
# 1->2->3->null, n = 3, return 2->3->null



class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        tmp_head = self.head
        while(tmp_head != None):
            print(tmp_head.data, end = ' ')
            tmp_head = tmp_head.next
    
    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):
             
            # If count of nodes in the
            # given list is less than 'n'
            if(second.next == None):
                 
                # If index = n then
                # delete the head node
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next
         
        while(second.next != None):
            second = second.next
            first = first.next
         
        first.next = first.next.next
    


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
print("Created Linked list is:")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion is:")
llist.printList()