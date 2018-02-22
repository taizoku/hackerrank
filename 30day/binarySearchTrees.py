class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        # print(root.data)
        leftHeight = rightHeight = 1
        if root.left is not None:
            leftHeight = self.getHeight(root.left)
            print("L:", leftHeight)
        if root.right is not None:
            rightHeight = rightHeight + self.getHeight(root.right)
            print("R:", rightHeight)
        # heightLeft = float('-inf') if not root.left
        # heightRight = float('-inf') if not root.left
        # print("L:", leftHeight, "R:", rightHeight)
        height = max(leftHeight, rightHeight)
        return height


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
