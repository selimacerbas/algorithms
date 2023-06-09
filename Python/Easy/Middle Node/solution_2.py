class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

#O(n) time | O(1) space - where n is the number of the nodes in the linked list.
def middleNode(linkedList):
    one = linkedList
    two = linkedList

    while two and two.next:
        two = two.next.next
        one = one.next
    
    return one

