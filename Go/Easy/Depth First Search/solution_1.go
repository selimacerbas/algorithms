package main

type Node struct {
	Children []*Node
	Name     string
}

func (n *Node) DepthFirstSearch(array []string) []string {
	array = append(array, n.Name)

	for _, child := range n.Children {

		array = child.DepthFirstSearch(array)

	}

	return array
}
