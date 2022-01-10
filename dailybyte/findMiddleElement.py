
def findMiddleElement():
    temp1 =  head
    temp2 = head
    count1 = count2 = 0
    while temp1 != None:
        count1 += 1
        temp1 = temp1.next
    middle = count1/2 - 1
    while count2 <= middle:
        count2 += 1
        temp2 = temp2.next
    
    return temp2