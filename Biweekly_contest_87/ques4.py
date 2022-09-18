from heapq import heapify,heappush,heappop
class Node:
    def __init__(self,giventrans):
        self.firstelement,self.secondelement=giventrans
    def __lt__(self,givenobject):
        return self.firstelement>givenobject.firstelement 
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        givenheap=[]
        for trans in transactions:
            givennode=Node(trans)
            heappush(givenheap,givennode)
        negativeelementssum=0
        for a,b in transactions:
            if a-b>0:
                negativeelementssum+=a-b
        finalans=0
        while(givenheap):
            element=givenheap.pop()
            
            difference=max(0,element.firstelement-element.secondelement)
            
            finalans=max(finalans,negativeelementssum-difference+element.firstelement)
        return finalans