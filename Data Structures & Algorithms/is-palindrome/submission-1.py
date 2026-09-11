import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        result = re.sub(r'[^a-zA-Z0-9]', '', s)
        if result==result[::-1]:
            return True
        else:
            return False
        
        