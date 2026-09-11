import re
import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        result = re.sub(r'[^a-zA-Z0-9]', '', s)
        first=0
        last=len(result)-1
        count=0
        while first<=last:
            if result[first]==result[last]:
                count+=1
                first+=1
                last-=1
            else:
                return False

        if count==math.ceil(len(result)/2):
            return True
            
        