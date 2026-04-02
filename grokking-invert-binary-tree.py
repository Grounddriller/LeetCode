from ds_v1.BinaryTree.BinaryTree import TreeNode

def mirror_binary_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    mirror_binary_tree(root.left)
    mirror_binary_tree(root.right)

    return root
