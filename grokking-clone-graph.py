from Node import *

def clone(root):
    if root is None:
        return None

    copies = {}

    def dfs(node):
        if node in copies:
            return copies[node]

        copy_node = Node(node.data)
        copies[node] = copy_node

        for neighbor in node.neighbors:
            copy_node.neighbors.append(dfs(neighbor))

        return copy_node

    return dfs(root)
