class Solution:
    def validPalindrome_internal(self,s,start,end,flag):
        if start>=end:
            return True
        if s[start]==s[end]:
            return self.validPalindrome_internal(s,start+1,end-1,flag)
        else:
            if flag==1:
                return False
            else:
                return self.validPalindrome_internal(s,start+1,end,1) or self.validPalindrome_internal(s,start,end-1,1)
    def validPalindrome(self, s):
        return self.validPalindrome_internal(s,0,len(s)-1,0)
sol=Solution()
s = "aba"
s = "abca"
s = "abc"
print(sol.validPalindrome(s))