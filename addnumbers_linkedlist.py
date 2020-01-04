# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
class LinkedList:
    def __init__(self, root):
        self.head = root
    def addNode(self, node):
        temp = self.head
        self.head=node
        self.head.next=temp

    def printList(self):
        while self.head:
            print(self.head.val)
            self.head = self.head.next    
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode(0)
        head_begin=l3
        prev_carry=0
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            val, carry = (prev_carry+x + y) % 10, (prev_carry+x + y)//10
            l3.next = ListNode((val)%10)
            l3=l3.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            prev_carry = carry
        if carry > 0:
            l3.next = ListNode(carry)
        return head_begin.next


if __name__ == "__main__":
    """
    node1 = ListNode(2)
    node2 = ListNode(3)
    ll = LinkedList(node1)
    ll.addNode(node2)
    ll.printList()
    """
    s = Solution()
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next=n2
    n2.next=n3

    m1 = ListNode(5)
    m2 = ListNode(6)
    m3 = ListNode(4)
    m1.next=m2
    m2.next=m3

    s.addTwoNumbers(n1,m1)