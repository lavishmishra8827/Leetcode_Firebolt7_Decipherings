class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        def updatedict(givenitem,finaldict):
            for item,value in givenitem:
                if item not in finaldict:
                    finaldict[item]=0
                finaldict[item]+=value
        finaldict={}
        updatedict(items1,finaldict)
        updatedict(items2,finaldict)
        finalans=[]
        for key in sorted(finaldict.keys()):
            finalans.append([key,finaldict[key]])
        return finalans