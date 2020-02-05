# Binary Search Tree  
Implementation defined in Introduction to Algorithms by Cormen et. al.

---

Usage:  
`python3 bst.py`

Available Methods:
- `_transplant(self, parent: Node, child: Node)` - Moves a subtree
- `insert(self, value: int)` - Inserts a value into the BST
- `max(self, x: Node = None) -> Node` - Returns a pointer to the maximum value of the BST
- `min(self, x: Node = None) -> Node` - Returns a pointer to the minimum value of the BST
- `search(self, value: int) -> Node` - Searches for the value in the BST
- ` print(self, node: Node)` - Prints the tree, effectively performing in-order traversal
- `delete(self, node: Node)` - Deletes a node from the BST
- `successor(self, node: Node) -> Node` - Finds the successor of the given node. i.e. the smallest key
- `predecessor(self, node: Node) -> Node` - Finds the predecessor of the given node  

Examples:
```python
from bst import Tree

tree = Tree()
[tree.insert(x) for x in range(1, 16)]

node = tree.search(5)

tree.delete(node)

tree.print(tree.root)
```