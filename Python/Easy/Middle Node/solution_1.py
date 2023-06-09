class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

def middleNode(linkedList):
    count = 0
    currentNode = linkedList

    while currentNode is not None:
        currentNode = currentNode.next
        count += 1
    
    middleNode = linkedList

    for _ in range(count // 2):
        middleNode = middleNode.next
    
    return middleNode
    
    


