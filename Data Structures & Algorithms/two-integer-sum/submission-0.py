class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1={}
        list2=[]
        
        for i,num in enumerate(nums):

            complement=target-num
            if complement not in dict1:
                dict1[num]=i
            else:
                list2.append(dict1[complement])
                list2.append(i)

        return list2


        