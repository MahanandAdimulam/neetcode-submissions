class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        encode = '#'
        for val in strs:
            res+=str(len(val))+encode+val
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        t = ''
        decode='#'
        i = 0
        while i <len(s):
            j=i
            while s[j]!=decode:
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i=j+length+1
        return res