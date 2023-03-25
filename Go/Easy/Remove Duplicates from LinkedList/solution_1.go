package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func RemoveDuplicatesFromLinkedList(linkedList *LinkedList) *LinkedList {

	currentNode := linkedList

	for currentNode != nil {

		nextNode := currentNode.Next

		for nextNode != nil && nextNode.Value == currentNode.Value {

			nextNode = nextNode.Next
		}

		currentNode.Next = nextNode
		currentNode = nextNode

	}

	return linkedList

}
