# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
# Time complexity : O(n)
# Space complexity : O(n)  




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            need = target-nums[i]
            if need in seen:
                return [seen[need],i]
            seen[nums[i]] = i    
            

        
