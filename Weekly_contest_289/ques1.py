class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if k==1:
            return s 
        while(True):
            if len(s)<=k:
                return s
            index_now=0
            ctr=0
            new_str=""
            while(index_now<len(s)):
                currsum=0
                ctr=0
                while(index_now<len(s) and ctr<k):
                    currsum+=int(s[index_now])
                    index_now+=1
                    ctr+=1
                #print(index_now)
                new_str+=str(currsum)
            s=new_str
sol=Solution()
s = "11111222223"
k = 3
print(sol.digitSum(s,k))