import copy
class Solution:
    def permuteUnique(self, nums):
        if len(nums)<2:
            return [nums]
        if len(nums)==2:
            if nums[0]!=nums[1]:
                return [nums,[nums[1],nums[0]]]
            else:
                return [nums]
        first=nums[0]
        remaining_list=self.permuteUnique(nums[1:])
        final_list=[]
        for j in remaining_list:
            '''
            new_list=copy.deepcopy(first)
            new_list.extend(j)
            final_list.append(new_list)
            new_list=copy.deepcopy(j)
            new_list.extend(first)
            final_list.append(new_list)
            '''
            for k in range(len(j)+1):
                j.insert(k,first)
                to_append=copy.deepcopy(j)
                if to_append not in final_list:
                    final_list.append(to_append)
                j.pop(k)
        return final_list