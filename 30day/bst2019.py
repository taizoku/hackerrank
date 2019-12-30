"""
https://www.hackerrank.com/challenges/30-binary-trees/problem
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
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
        queue = []
        #Write your code here
        if root:  # root not empty
            queue.append(root)

        while queue:  # while queue is not empty
            del queue[0]  # dequeue

            # process tree's root
            print(root)
            
            # enqueue child elements from next level in order
            if root.left:
                queue.append(root.left)
                print(root.left.data)
            elif root.right:
                queue.append(root.right)
                print(root.right.data)

T=int(input())
s = Solution()
for i in range(T):
    
    s.insert(int(input()))
print(s)
