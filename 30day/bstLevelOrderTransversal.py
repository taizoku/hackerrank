import sys

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root is not None:
            return Node(data)

        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur

            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        queue = []
        # append root
        queue.append(root)

        # level down left
        if root.left is not None:
            queue.append(root.left)

        # level down

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
