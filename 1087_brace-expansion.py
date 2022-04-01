class Solution:
    def expand(self, s):
        given_str=""
        i=0
        final_list=[]
        while(i<len(s)):
            if s[i]=='{':
                if given_str!='':
                    final_list.append(given_str)
                    given_str=''
                i+=1
                #new_list=[]
                start=i
                while(s[i]!='}'):
                    #new_list.append(s[i])
                    i+=1
                end=i-1
                new_list=s[start:end+1].split(",")
                new_list.sort()
                final_list.append(new_list)
            else:
                given_str+=s[i]
            i+=1
        if given_str!='':
            final_list.append(given_str)
        ans_list=[]
        def expand_internal(str_now,index):
            if index==len(final_list):
                print(str_now)
                ans_list.append(str_now)
                return
            if type(final_list[index])==list:
                for i in final_list[index]:
                    expand_internal(str_now+i,index+1)
            else:
                expand_internal(str_now+final_list[index],index+1)
        expand_internal("",0)
        return ans_list
sol=Solution()
s = "{a,b}c{e,d}f"
s = "abcd"
print(sol.expand(s))