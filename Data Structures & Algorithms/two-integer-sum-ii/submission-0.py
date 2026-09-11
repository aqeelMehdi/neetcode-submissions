class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list1=[]
        first=1
        last=len(numbers)
        while first<last:

            if (numbers[first-1]+numbers[last-1]>target):
                last-=1
            elif (numbers[first-1]+numbers[last-1]<target):
                first+=1
            else:
                list1.append(first)
                list1.append(last)
                return list1

        