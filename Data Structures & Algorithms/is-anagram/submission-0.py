class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check len
        if len(s)!=len(t):
            return False
        #create hash maps
        countS,countT={},{}

        #add val and their count to hash maps
        for i in range (len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
            #iterate thru hash maps to make sure counts r same
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
            
        return True    



