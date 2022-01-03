# Problem - Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# 
# Example 2:
# Input: root = []
# Output: []
#
# Example 3:
# Input: root = [1]
# Output: [1]
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # Insert method for new Node
    def insert(self, val):
        if self.val:
            # Creates a new node if the val is None
            if not val:
                return TreeNode(val)

            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
                    
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
                    
            else:
                self.val = val

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            ans = self.inorderTraversal(root.left)
            ans.append(root.val)
            ans = ans + self.inorderTraversal(root.right)
        return ans
    
def main():
    root = TreeNode(1)
    root.insert(None)
    root.insert(2)
    root.insert(3)
    
    ans = Solution().inorderTraversal(root=root)
    print(ans) # Expected result [1, 3, 2]

if __name__ == '__main__':
    main()
    