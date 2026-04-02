from collections import deque
from ds_v1.BinaryTree.BinaryTree import TreeNode

def zigzag_level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if left_to_right:
                level.append(node.data)
            else:
                level.appendleft(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result
