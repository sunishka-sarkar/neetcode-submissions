class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+=str(len(s))+"#"+s
        return result
        

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j]) #extract length of the string
            result.append(s[j+1:j+1+length]) #extracting the string itself
            i=j+1+length  #move i to the next string len
        return result
        
