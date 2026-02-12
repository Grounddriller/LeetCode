# ----------------
# Binary Tree Node
# ----------------
class Node:
    def __init__(self, val):
        self.val = val        # Value stored in this node
        self.left = None     # Reference to the left child
        self.right = None    # Reference to the right child


# -----------------------------------------
# Iterative Depth-First Search (Preorder)
# -----------------------------------------
def dfs_preorder(root):
    # If the tree is empty, there is nothing to traverse
    if not root:
        return

    # Stack used to manually control DFS traversal
    # Starts with the root node
    stack = [root]

    # Continue until there are no nodes left to visit
    while stack:
        # Show current stack contents (for demo clarity)
        print("Stack:", [node.val for node in stack])

        # Remove the last node added to the stack (LIFO)
        node = stack.pop()

        # Visit the node
        # Preorder means: Root -> Left -> Right
        print("Visit:", node.val)

        # Push right child first
        # so the left child is processed first
        if node.right:
            stack.append(node.right)

        # Push left child second
        if node.left:
            stack.append(node.left)

        print("----")


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

    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")

    # Connect nodes
    A.left = B
    A.right = C
    B.left = D
    B.right = E

    # Run the DFS demo
    dfs_preorder(A)
