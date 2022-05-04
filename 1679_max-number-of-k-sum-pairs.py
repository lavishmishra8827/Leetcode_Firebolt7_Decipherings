class Solution:
    def maxOperations(self, nums, k):
        nums_freq_dict={}
        total_pairs=0
        for i in nums:
            if i not in nums_freq_dict:
                nums_freq_dict[i]=0
            nums_freq_dict[i]+=1
        if k%2==0 and k//2 in nums:
            total_pairs+=nums_freq_dict[k//2]//2
            del nums_freq_dict[k//2]
            #print(k//2 in nums_freq_dict)
        for key in nums_freq_dict.keys():
            if k-key in nums_freq_dict:
                minimum_values=min(nums_freq_dict[key],nums_freq_dict[k-key])
                #print(key,k-key,minimum_values)
                nums_freq_dict[key]-=minimum_values
                nums_freq_dict[k-key]-=minimum_values
                total_pairs+=minimum_values
        return total_pairs
sol=Solution()
nums = [1,2,3,4]
k = 5
#nums = [3,1,3,4,3]
#k = 6
print(sol.maxOperations(nums,k))