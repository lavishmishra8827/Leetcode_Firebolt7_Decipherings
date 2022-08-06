class Solution:
    
    def countBadPairs(self, nums: List[int]) -> int:
        def nc2(n):
            return (n*(n-1))//2
        freqdict={}
        for index,number in enumerate(nums):
            tostore=index-number
            if tostore not in freqdict:
                freqdict[tostore]=0
            freqdict[tostore]+=1
        goodpairs=0
        for value in freqdict.values():
            goodpairs+=nc2(value)
        return nc2(len(nums))-goodpairs
    