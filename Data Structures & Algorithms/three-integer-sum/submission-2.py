class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            else:
                l,r=i+1,len(nums)-1
                while l<r:
                    threeSum=a+nums[l]+nums[r]
                    if threeSum>0:
                        r-=1
                    elif threeSum<0:
                        l+=1
                    else:
                        res.append([a,nums[l],nums[r]])
                        # res.append([a, nums[l], nums[r]])
                        # Move both pointers
                        l += 1
                        r -= 1
                        # # Skip duplicate left values
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res

        