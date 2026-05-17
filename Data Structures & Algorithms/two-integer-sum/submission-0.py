class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        n = len(nums)
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in index_map:
                return [index_map[remaining],i]
            else:
                index_map[nums[i]] = i
            



            
             
