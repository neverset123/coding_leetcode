from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

class Solution:

    def diameter(self, root):
        return self.maxDepth(root.left)+self.maxDepth(root.right)

    def maxDepth(self, root):
        if root==None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return max(left_depth, right_depth)+1

if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().diameter(test_tree))