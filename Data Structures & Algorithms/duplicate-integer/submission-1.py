class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=0
        nums.sort()
        for i in range(1,len(nums)):

            if nums[i-1]==nums[i]:
                check=1
                return True

            
        if (check==0):
            return False





