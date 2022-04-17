class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq_dict={}
        for i in tasks:
            if i not in freq_dict:
                freq_dict[i]=0
            freq_dict[i]+=1
        rounds=0
        for key,value in freq_dict.items():
            if value==1:
                return -1
            else:
                rounds+=value//3
            if value%3!=0:
                rounds+=1
        return rounds