'''
import time
def ispalindrome(number):
    string=str(number)
    reverse=string[::-1]
    #print(string,reverse)
    if reverse==string:
        return True
    return False
#print(ispalindrome(111))
#print(ispalindrome(112))
start_time=time.time()
for i in range(100000000000000,1000000000000000):
    if ispalindrome(i):
        print(i)
end_time=time.time()
print(end_time-start_time)
'''
class Solution:
    '''
    def ispalindrome(self,number):
        string=str(number)
        reverse=string[::-1]
        #print(string,reverse)
        if reverse==string:
            return True
        return False
    
    def kthPalindrome_internal(self,done,even,string_now,length_needed,queries,index,palindrome_index_now,answer):
        if done:
            return done,index,palindrome_index_now
        if length_needed==0:
            for i in range(10):
                to_add=str(i)
                if even:
                    to_add=2*to_add
                #print(to_add)
                palindrome_string=string_now+to_add+string_now[::-1]
                palindrome_index_now+=1
                if palindrome_index_now==queries[index]:
                    index+=1
                    print(palindrome_index_now,palindrome_string)
                    answer.append(int(palindrome_string))
                    if index==len(queries):
                        done=True
                        break
                #print(palindrome_index_now,palindrome_string)
        else:
            for i in range(10):
                done,index,palindrome_index_now=self.kthPalindrome_internal(done,even,string_now+str(i),length_needed-1,queries,index,palindrome_index_now,answer)
        return done,index,palindrome_index_now
    def kthPalindrome(self, queries, intLength):
        if intLength==1:
            palindromes=[]
            for i in range(1,10):
                if self.ispalindrome(i):
                   palindromes.append(i)
            if len(palindromes)<max(queries):
                return -1
            ans=[]
            for i in queries:
                ans.append(palindromes[i-1])
            return ans
            
        if intLength==2:
            palindromes=[]
            for i in range(1,100):
                if self.ispalindrome(i):
                    palindromes.append(i)
            if len(palindromes)<max(queries):
                return -1
            ans=[]
            for i in queries:
                ans.append(palindromes[i-1])
            return ans
            
        if intLength%2==0:
            even=True
        else:
            even=False
        index=0
        palindrome_index_now=0
        done=False
        answer=[]
        for i in range(1,10):
            string_now=str(i)
            length_needed=(intLength-1)//2-1
            done,index,palindrome_index_now=self.kthPalindrome_internal(done,even,string_now,length_needed,queries,index,palindrome_index_now,answer)
        if done:
            return answer
        else:
            return -1
    '''
    def find_palindrome(self,number,intLength):
        string=str(number)
        rem_length=intLength-len(string)
        new_string=string[:rem_length]
        final_number=string+new_string[::-1]
        return int(final_number)
        
    def kthPalindrome(self, queries, intLength):
        string='1'
        needed_zeroes=(intLength+1)//2-1
        for i in range(needed_zeroes):
            string+='0'
        #print(string)
        number=int(string)
        x=len(string)
        ans=[]
        
        for i in queries:
            temp=number+i-1
            #print(temp)
            if len(str(temp))==x:
                ans.append(self.find_palindrome(temp,intLength))
            else:
                ans.append(-1)
            #number=int(string)
        return ans
sol=Solution()
queries = [1,2,3,4,5,90]
intLength = 3
queries = [2,4,6]
intLength = 4
queries=[1,10]
intLength=1
queries=[3,44,5,6]
intLength=2
print(sol.kthPalindrome(queries, intLength))
