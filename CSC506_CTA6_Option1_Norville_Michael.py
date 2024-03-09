"""
@author: Michael Norville
CSC506 - Critical Thinking Assignment 6 - Option 1

Build simple binary search tree. Build Node and Tree classes. Write a #build_tree 
method that takes an array of data [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
and turns it into a balanced binary tree full of Node objects appropriately placed 
(don't forget to sort and remove duplicates!). The #build_tree method should 
return the level-1 root node. Write an #insert and #delete method which accepts 
a value to insert/delete.
"""
#Build Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Build Tree Class
class Tree:
    def __init__(self, arr):
        self.root = self.build_tree(arr)
        
    #Build_tree Method
    def build_tree(self, arr):
        if not arr:
            return None
        arr = sorted(set(arr)) #sorts and removes duplicates
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.build_tree(arr[:mid])
        root.right = self.build_tree(arr[mid + 1:])
        return root

#Insert Method - Code copied from zyBooks 6.11
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current_node = self.root
            while current_node is not None:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = Node(value)
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = Node(value)
                        current_node = None
                    else:
                        current_node = current_node.right

#Delete Method - Code copied from zyBooks 6.11
    def remove(self, value):
        parent = None
        current_node = self.root
        
        # Search for the node.
        while current_node is not None:
        
            # Check if current_node has a matching value.
            if current_node.value == value: 
                if current_node.left is None and current_node.right is None:   # Case 1
                    if parent is None: # Node is root
                        self.root = None
                    elif parent.left is current_node: 
                        parent.left = None
                    else:
                        parent.right = None
                    return  # Node found and removed
                elif current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node: 
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed
                elif current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None: # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed
                else:                                    # Case 3
                    # Find successor (leftmost child of right subtree)
                    successor_parent = current_node
                    successor = current_node.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    current_node.value = successor.value      # Copy successor to current node
                    if successor_parent == current_node:
                        successor_parent.right = successor.right     # Remove successor from right subtree
                    else:
                        successor_parent.left = successor.left
                    return
            elif current_node.value < value: # Search right
                parent = current_node
                current_node = current_node.right
            else:                        # Search left
                parent = current_node
                current_node = current_node.left
        return # Node not found

    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.value)
            result += self.inorder_traversal(root.right)
        return result

#Using above classes and methods
arr = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
BST = Tree(arr)
print(BST.inorder_traversal(BST.root))
BST.insert(21)
print(BST.inorder_traversal(BST.root))
BST.remove(7)
print(BST.inorder_traversal(BST.root))