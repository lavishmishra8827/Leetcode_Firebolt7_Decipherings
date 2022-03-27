import math
class Solution:
    def maxValueOfCoins(self, piles, k):
        piles_length=len(piles)
        #print(piles_length)
        @lru_cache(None)
        def dp(i,k_remaining):
            
            if i==piles_length:
                #print("k_remaining",k_remaining)
                if k_remaining==0:
                    return 0
                else:
                    return -math.inf
            ans_now=dp(i+1,k_remaining)
            sum_now=0
            for j in range(min(k_remaining,len(piles[i]))):
                sum_now+=piles[i][j]
                #print("i,j,sumnow",i,j,sum_now,dp(i+1,k_remaining-j-1))
                #print("second_expression",sum_now,sum_now+dp(i+1,k_remaining-j-1))
                ans_now=max(ans_now,sum_now+dp(i+1,k_remaining-j-1))
            #print(i,k_remaining,ans_now)
            
            return ans_now
            
        return dp(0,k)
sol=Solution()
piles = [[1,100,3],[7,8,9]]
k = 2
print(sol.maxValueOfCoins(piles,k))