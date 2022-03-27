class Solution:
    def find_difference(self,dict1,dict2):
        additions_req=0
        for key,value in dict1.items():
            if key not in dict2:
                additions_req+=value
            elif value>dict2[key]:
                additions_req+=value-dict2[key]
        return additions_req
                
    def minSteps(self, s: str, t: str) -> int:
        freq_dict_s={}
        freq_dict_t={}
        for i in s:
            if i not in freq_dict_s:
                freq_dict_s[i]=0
            freq_dict_s[i]+=1
        for i in t:
            if i not in freq_dict_t:
                freq_dict_t[i]=0
            freq_dict_t[i]+=1
        print(freq_dict_s)
        print(freq_dict_t)
        a = self.find_difference(freq_dict_s,freq_dict_t)
        b = self.find_difference(freq_dict_t,freq_dict_s)
        print(a,b)
        return a+b
sol=Solution()
s="cotxazilut"
t="nahrrmcchxwrieqqdwdpneitkxgnt"

print(sol.minSteps(s,t))        