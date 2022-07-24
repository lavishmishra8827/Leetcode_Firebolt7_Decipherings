from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.indexdict={}
        self.numbertoindexmapping={}

    def change(self, index: int, number: int) -> None:
        if index not in self.indexdict:
            self.indexdict[index]=number
            if number not in self.numbertoindexmapping:
                self.numbertoindexmapping[number]=SortedSet()
            self.numbertoindexmapping[number].add(index)
        else:
            prevnumber=self.indexdict[index]
            if prevnumber==number:
                return 
            self.indexdict[index]=number
            if number not in self.numbertoindexmapping:
                self.numbertoindexmapping[number]=SortedSet()
            self.numbertoindexmapping[number].add(index)
            #print(self.numbertoindexmapping[prevnumber])
            self.numbertoindexmapping[prevnumber].remove(index)
        

    def find(self, number: int) -> int:
        if number in self.numbertoindexmapping and self.numbertoindexmapping[number]:
            return self.numbertoindexmapping[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)