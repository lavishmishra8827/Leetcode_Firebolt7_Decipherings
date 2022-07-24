class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        ranks_set=set(ranks)
        freq_dict={}
        maxvalue=0
        for item in ranks:
            if item not in freq_dict:
                freq_dict[item]=0
            freq_dict[item]+=1
            maxvalue=max(maxvalue,freq_dict[item])
        if maxvalue>=3:
            return "Three of a Kind"
        if maxvalue==2:
            return "Pair"
        return "High Card"