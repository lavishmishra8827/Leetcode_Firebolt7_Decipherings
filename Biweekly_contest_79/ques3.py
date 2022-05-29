class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        number_of_edges={}
        for i in range(n):
            number_of_edges[i]=0
        for a,b in roads:
            number_of_edges[a]+=1
            number_of_edges[b]+=1
        #print(number_of_edges)
        values_list=list(number_of_edges.values())
        values_list.sort()
        #print(values_list)
        final_sum=0
        for i in range(len(values_list)):
            final_sum+=(i+1)*values_list[i]
        return final_sum