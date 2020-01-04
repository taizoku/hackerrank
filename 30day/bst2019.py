"""
https://www.hackerrank.com/challenges/30-binary-trees/problem
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        # as long as the bst is not empty
        queue = []
        #Write your code here
        if root:  # root not empty
            queue.append(root.data)  # enqueue current root
            print(root.data)

        while queue:  # while queue is not empty
            del queue[0]  # dequeue

            # process tree's root
            root = root.left
            # go left, go back to root
            # go right, go back to root
            # next level (go left) and repeat
            root = root.right
            
            # enqueue child elements from next level in order
            if root.left:
                queue.append(root.left)
                print(root.left.data)
            elif root.right:
                queue.append(root.right)
                print(root.right.data)

#T=int(input())
s = Solution()

head = s.insert(None, 3)
l = s.insert(head, 2)
r = s.insert(head, 5)
s.insert(l, 1)
s.insert(r, 4)
s.insert(r, 7)
s.levelOrder(head)
