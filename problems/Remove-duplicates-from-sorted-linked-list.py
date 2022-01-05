# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#
# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
#
# Example 2:
# 
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self, head=None):
        self.head = head
 
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.val)
            temp = temp.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # do nothing if the list is empty
        if head is None:
            return None

        current = head

        # compare the current node with the next node
        while current.next:
            if current.val == current.next.val:
                nextNode = current.next.next
                current.next = nextNode
            else:
                current = current.next        # only advance if no deletion

        return head
    
def main():
    # Constructing the first example linked list
    n3 = ListNode(val=2, next=None)
    n2 = ListNode(val=1, next=n3)
    list1 = ListNode(1, next=n2)
    
    # Constructing the second example linked list
    n4 = ListNode(val=4, next=None)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)
    list2 = ListNode(val=1, next=n1)

    # Remove duplicates from a sorted linked list
    ans1 = Solution().deleteDuplicates(head=list1)   
    LinkedList(head=ans1).printList() # Expected = [1,2]
    
    ans2 = Solution().deleteDuplicates(head=list2)   
    LinkedList(head=ans2).printList() # Expected = [1,2, 3]
    
if __name__ == '__main__':
    main()
    