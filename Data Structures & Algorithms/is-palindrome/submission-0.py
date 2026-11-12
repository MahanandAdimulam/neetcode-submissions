class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < len(s):
            if s[start].isalnum() is False:
                start+=1
            elif s[end].isalnum() is False:
                end-=1
            elif s[start].lower()==s[end].lower():
                start+=1
                end-=1
            elif s[start].lower()!=s[end].lower():
                return False
        return True