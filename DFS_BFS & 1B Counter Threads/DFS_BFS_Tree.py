from collections import deque  # We import deque to use as a queue for BFS

# Node class definition

class Node:
    def __init__(self, data):
        # Each node has a value, and left/right children
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert a value into the binary search tree.
        Smaller values go to the left,
        larger values go to the right.
        """
        if data < self.data:
            # If the left child does not exist, create it
            if self.left is None:
                self.left = Node(data)
            else:
                # Otherwise, keep recursing down the left subtree
                self.left.insert(data)

        elif data > self.data:
            # If the right child does not exist, create it
            if self.right is None:
                self.right = Node(data)
            else:
                # Otherwise, keep recursing down the right subtree
                self.right.insert(data)


# Depth First Search (DFS)
# Preorder traversal (Root -> Left -> Right)

def dfs_preorder(root):
    """
    Visit nodes in depth-first preorder.
    That means:
      1. Process the current node
      2. Recurse on left subtree
      3. Recurse on right subtree
    """
    if root:
        # Print the current node’s value
        print(root.data, end=" ")

        # Visit left side next
        dfs_preorder(root.left)

        # Then visit right side
        dfs_preorder(root.right)


# Breadth First Search (BFS)
# Level order traversal

def bfs(root):
    """
    Visit nodes level by level using a queue.
    Starts at the root, then its children, then grandchildren, etc.
    """
    if not root:
        return

    # Initialize the queue with the root node
    queue = deque([root])

    # Loop until the queue is empty
    while queue:
        # Remove a node from the front of the queue
        current = queue.popleft()

        # Print its value
        print(current.data, end=" ")

        # Add the left child, if it exists
        if current.left:
            queue.append(current.left)

        # Add the right child, if it exists
        if current.right:
            queue.append(current.right)

# Build a BST with 20 values

values = [15, 6, 23, 4, 7, 71, 5, 50, 3, 10, 8, 11, 1, 2, 9, 12, 16, 70, 60, 55]

# The first value becomes the root of the BST
root = Node(values[0])

# Insert the remaining values
for v in values[1:]:
    root.insert(v)


# -------------------------
# Run both traversals
# -------------------------
print("DFS (Preorder - Depth First):")
dfs_preorder(root)

print("\n\nBFS (Level Order - Breadth First):")
bfs(root)
