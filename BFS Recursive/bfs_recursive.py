from collections import deque   # deque gives us an efficient queue (O(1) popleft)


# ----------------
# Binary Tree Node 
# ----------------
class Node:
    def __init__(self, val):
        self.val = val          # Value stored in the node
        self.left = None       # Reference to left child
        self.right = None      # Reference to right child


# -----------------------------------------
# Recursive Breadth-First Search (BFS)
# -----------------------------------------
def bfs_recursive(queue):
    # Base case:
    # If the queue is empty, there are no more nodes to process
    if not queue:
        return

    # Remove the node at the front of the queue (FIFO behavior)
    node = queue.popleft()

    # Visit the node
    # BFS visits nodes level by level
    print(node.val)

    # If the node has a left child,
    # add it to the end of the queue
    if node.left:
        queue.append(node.left)

    # If the node has a right child,
    # add it to the end of the queue
    if node.right:
        queue.append(node.right)

    # Recursive call:
    # Process the next node in the queue
    bfs_recursive(queue)


# -----------------------------
# Demo / Entry Point
# -----------------------------
if __name__ == "__main__":
    # Build the tree:
    #
    #        A
    #       / \
    #      B   C
    #     / \
    #    D   E

    A = Node("A")              # Create root node
    B = Node("B")              # Create child nodes
    C = Node("C")
    D = Node("D")
    E = Node("E")

    # Connect nodes to form the tree
    A.left = B                 # A -> left -> B
    A.right = C                # A -> right -> C
    B.left = D                 # B -> left -> D
    B.right = E                # B -> right -> E

    # Initialize the queue with the root node
    queue = deque([A])

    # Start recursive BFS traversal
    bfs_recursive(queue)
