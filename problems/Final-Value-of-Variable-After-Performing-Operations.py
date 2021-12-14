# There is a programming language with only four operations and one variable X:
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
#
# Example 1:
# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.
#
# Example 2:
# Input: operations = ["++X","++X","X++"]
# Output: 3
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# ++X: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# X++: X is incremented by 1, X = 2 + 1 = 3.
#
# Example 3:
# Input: operations = ["X++","++X","--X","X--"]
# Output: 0
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# X++: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# --X: X is decremented by 1, X = 2 - 1 = 1.
# X--: X is decremented by 1, X = 1 - 1 = 0.
#
# Constraints:
# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".

from typing import List 

class Solution:
    """
    Python Class used to find the final value of a variable after performing python operations. 
    """
    def __init__(self):
        # Initialize X with a value of 0
        self.X = 0
        
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Uses If and Else-If Statements to determine the correct python operation

        Args:
            operations (List[str]): A List containing strings used to determine the correct python operation

        Returns:
            int: The final value of X after all operations are performed
        """
        for element in operations:
            if element == "--X":
                self.X -= 1
            elif element == "X--":
                self.X -= 1
            elif element == "++X":
                self.X += 1
            elif element == "X++":
                self.X += 1
        return self.X
    
if __name__ == '__main__':
    operations1 = ["--X","X++","X++"]
    ans1 = Solution().finalValueAfterOperations(operations1)
    print(ans1) # Expected 1
    
    operations2 = ["++X","++X","X++"]
    ans2 = Solution().finalValueAfterOperations(operations2)
    print(ans2) # Expected 3
    
    operations3 = ["X++","++X","--X","X--"]
    ans3 = Solution().finalValueAfterOperations(operations3)
    print(ans3) # Expected 0