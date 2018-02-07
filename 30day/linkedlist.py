class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(self, data)
        new_node.next = None
        current = head
        if current is not None:
            while current.next is not None:
                current = current.next
        current.next = new_node

        return head


myList = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)
myList.display(head);