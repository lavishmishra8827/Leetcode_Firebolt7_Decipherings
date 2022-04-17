class Solution:
    def minimumCost(self, cost):
        cost.sort()
        number=1
        index=len(cost)-1
        given_sum=0
        while(index>=0):
            if number%3==0:
                index-=1
                number+=1
                continue
            #print(index)
            given_sum+=cost[index]
            index-=1
            number+=1
        return given_sum
if __name__=="__main__":
    sol=Solution()
    cost = [6,5,7,9,2,2]
    cost = [5,5]
    cost = [1,2,3]
    print(sol.minimumCost(cost))