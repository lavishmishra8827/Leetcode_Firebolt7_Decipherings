class ATM:

    def __init__(self):
        self.note_dict={}
        self.note_dict[20]=0
        self.note_dict[50]=0
        self.note_dict[100]=0
        self.note_dict[200]=0
        self.note_dict[500]=0
        
    def deposit(self, banknotesCount: List[int]) -> None:
        self.note_dict[20]+=banknotesCount[0]
        self.note_dict[50]+=banknotesCount[1]
        self.note_dict[100]+=banknotesCount[2]
        self.note_dict[200]+=banknotesCount[3]
        self.note_dict[500]+=banknotesCount[4]
        
    def withdraw(self, amount: int) -> List[int]:
        given_list=[500,200,100,50,20]
        return_list=[]
        for note in given_list:
            max_needed=amount//note
            max_avl=self.note_dict[note]
            reduce=min(max_needed,max_avl)
            amount-=reduce*note
            return_list.insert(0,reduce)
            if amount==0:
                break
        else:
            return [-1]
        while(len(return_list)!=5):
            return_list.insert(0,0)
        self.note_dict[20]-=return_list[0]
        self.note_dict[50]-=return_list[1]
        self.note_dict[100]-=return_list[2]
        self.note_dict[200]-=return_list[3]
        self.note_dict[500]-=return_list[4]
        #print(return_list)
        return return_list
        

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)