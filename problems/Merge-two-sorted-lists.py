# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# 
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while True:
            
            # If any of the linked List become empty join all elements of the other list
            if list1 is None:
                tail.next = list2
                break
                
            if list2 is None:
                tail.next = list1
                break
            
            # compare the data of the lists and whichever is smaller 
            # append to the last of the merge list and the head is changed                
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
        
        return dummy.next
       
        
def main():
    # Constructing the first linked list
    n3 = ListNode(val=4, next=None)
    n2 = ListNode(val=2, next=n3)
    list1 = ListNode(1, next=n2)
    
    # Constructing the second linked list
    n3 = ListNode(val=4, next=None)
    n2 = ListNode(val=3, next=n3)
    list2 = ListNode(val=1, next=n2)
    
    # Merge the two sorted linked list
    ans = Solution().mergeTwoLists(list1, list2)   
    LinkedList(head=ans).printList() # Expected = [1,1,2,3,4,4]
    

if __name__ == '__main__':
    main()
    
    