class Solution:
    def sortEvenOdd(self, nums):
        i=0
        even_index_list=[]
        odd_index_list=[]
        while(i<len(nums)):
            if i%2==0:
                even_index_list.append(nums[i])
            else:
                odd_index_list.append(nums[i])
            i+=1
        even_index_list.sort()
        odd_index_list.sort(reverse=True)
        i=0
        final_list=[]
        while(i<len(odd_index_list) and i<len(even_index_list)):
            final_list.append(even_index_list[i])
            final_list.append(odd_index_list[i])
            i+=1
        while(i<len(odd_index_list)):
            final_list.append(odd_index_list[i])
            i+=1
        while(i<len(even_index_list)):
            final_list.append(even_index_list[i])
            i+=1
        return final_list

if __name__=="__main__":
    sol=Solution()
    nums = [4,1,2,3]
    #nums = [2,1]
    nums = [1,2,3,4,5]
    print(sol.sortEvenOdd(nums))