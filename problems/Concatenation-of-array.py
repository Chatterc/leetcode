# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
#
# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
#
# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
#
# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000

from typing import List


class Solution:
    """
    Python Class the provides attributes and get method to concatenate two arrays of integers. 
    """
    
    def __init__(self):
        # Init empty python lists
        self.first_array = []
        self.second_array = []
        
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Get method to concatenate two arrays of integers

        Args:
            nums (List[int]): An array of integers

        Returns:
            List[int]: A concatenated array
        """
        
        # Travesal of an array of integers
        for i in range(len(nums)):
            self.first_array.append(nums[i])
            self.second_array.append(nums[i])
        
        # Python operator to concatenate two arrays 
        ans = self.first_array + self.second_array
        return ans
    

if __name__ == '__main__':
    
    test_case_1 = [1,2,1]
    ans_1 = Solution().getConcatenation(nums=test_case_1)
    print(ans_1)
    
    test_case_2 = [1,3,2,1]
    ans_2 = Solution().getConcatenation(nums=test_case_2)
    print(ans_2)
    
    # Expected
    # ans_1 = [1,2,1,1,2,1]
    # ans_2 = [1,3,2,1,1,3,2,1]