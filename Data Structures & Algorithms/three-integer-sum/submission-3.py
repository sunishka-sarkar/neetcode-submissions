class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array for 2 ptrs to work
        nums.sort()
        result=[]
        #skip duplicates
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            #fix the pointers l and r after fixing 1st number
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    #skip left dupes
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return result


        
        