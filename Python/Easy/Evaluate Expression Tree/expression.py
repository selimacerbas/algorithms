# This is an input class. Do not edit.
# Leaf nodes are nodes that does not have child node.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    operators = {
        -1: lambda x, y: x + y,
        -2: lambda x, y: x - y,
        -3: lambda x, y: int(x / y),
        -4: lambda x, y: x * y
    }

    if tree.value >= 0: # Return non negative.
        return tree.value

    left_val = evaluateExpressionTree(tree.left)
    right_val = evaluateExpressionTree(tree.right)
    
    return operators[tree.value](left_val, right_val)
    


# Could also be written like this; 

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluateExpressionTree(tree):
    if tree:
        left = evaluateExpressionTree(tree.left)
        right = evaluateExpressionTree(tree.right)
        operators = {
            -1: lambda: left + right,
            -2: lambda: left - right,
            -3: lambda: int(left / right),
            -4: lambda: left * right
        }
        return operators.get(tree.value, lambda: tree.value)