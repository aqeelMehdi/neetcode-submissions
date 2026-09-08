class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        suffix=1
        main_list=[]
        for i in range(len(nums)):
            main_list.append(prefix)
            prefix=prefix*nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            main_list[i]*=suffix
            suffix=suffix*nums[i]

        return main_list

        