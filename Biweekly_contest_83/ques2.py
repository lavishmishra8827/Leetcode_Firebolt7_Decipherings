class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def calculateforoccurence(n):
            return (n*(n+1))//2
        i=0
        occurence_now=0
        freq_dict={}
        while(i<len(nums)):
            if nums[i]==0:
                occurence_now+=1
            else:
                if occurence_now!=-0:
                    if occurence_now not in freq_dict:
                        freq_dict[occurence_now]=0
                    freq_dict[occurence_now]+=1
                    occurence_now=0
            i+=1
        if occurence_now!=0:
            if occurence_now not in freq_dict:
                freq_dict[occurence_now]=0
            freq_dict[occurence_now]+=1
        finalans=0
        for key,value in freq_dict.items():
            #print(key,value)
            finalans+=value*calculateforoccurence(key)
        return finalans