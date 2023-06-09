package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func MiddleNode(linkedList *LinkedList) *LinkedList {
	currentNode := linkedList
	count := 0

	for currentNode != nil {
		currentNode = currentNode.Next
		count += 1
	}

	middleNode := linkedList

	for i := 0; i < (count / 2); i++ {
		middleNode = middleNode.Next
	}

	return middleNode
}
