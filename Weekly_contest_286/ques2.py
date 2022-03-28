class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        index=0
        deletions=0
        i=1
        while(i<len(nums)):
            if index%2==0 and nums[i]==nums[i-1]:
                deletions+=1
            else:
                index=(index+1)%2
            i+=1
        #print(deletions)
        if (len(nums)-deletions)%2!=0:
            deletions+=1
        return deletions
                