from ds_v1.BinaryTree.BinaryTree import TreeNode

def serialize(root):
    result = []

    def dfs(node):
        if node is None:
            result.append(None)
            return

        result.append(node.data)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def deserialize(stream):
    index = 0

    def dfs():
        nonlocal index

        if stream[index] is None:
            index += 1
            return None

        node = TreeNode(stream[index])
        index += 1
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()
