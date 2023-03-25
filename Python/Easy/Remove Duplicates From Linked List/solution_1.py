class LinkedList:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):

    currentNode = linkedList

    while currentNode != None:
        nextNode = currentNode.next
        while nextNode != None and  nextNode.value == currentNode.value:
            nextNode = nextNode.next
        
        currentNode.next = nextNode
        currentNode = nextNode

    return linkedList

        