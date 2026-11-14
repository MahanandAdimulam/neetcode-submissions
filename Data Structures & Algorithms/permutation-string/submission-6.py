class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def l_s(s:str):
            ls=[]
            for c in s:
                ls.append(c)
            return ls 
        for l in range(len(s2)):
            if s2[l] in s1:
                ls=l_s(s1)
                ls.remove(s2[l])
                r=l+1
                while r<len(s2) and s2[r] in ls:
                    ls.remove(s2[r])
                    r+=1
                if r-l == len(s1) and ls==[]:
                    return True
        return False