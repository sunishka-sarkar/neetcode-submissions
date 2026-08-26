class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0    #lp
        max_length=0
        char_set=set()  #create set

        for r in range(len(s)):
            char=s[r]
            while char in char_set: 
                char_set.remove(s[l])  #if char alr exists shrink window
                l+=1
            char_set.add(char)
            curr_len=r-l+1
            max_length=max(max_length,curr_len)
        return max_length
    


        