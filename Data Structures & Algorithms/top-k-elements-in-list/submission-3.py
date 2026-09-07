class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        main_list=[]
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        sorted_nums = sorted(dict1, key=dict1.get, reverse=True)


        return sorted_nums[:k]

        