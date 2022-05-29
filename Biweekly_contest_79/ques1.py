class Solution:
    def digitCount(self, num: str) -> bool:
        freq_dict={}
        for i in range(len(num)):
            freq_dict[i]=0
        #print(freq_dict)
        for i in num:
            i=int(i)
            if i in freq_dict:
                freq_dict[i]+=1
        #print(freq_dict)
        for i in range(len(num)):
            if freq_dict[i]!=int(num[i]):
                return False
        return True