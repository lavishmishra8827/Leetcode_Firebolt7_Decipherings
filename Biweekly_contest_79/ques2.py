class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_word_count_dict={}
        for i in range(len(senders)):
            sender=senders[i]
            message=messages[i]
            if sender not in sender_word_count_dict:
                sender_word_count_dict[sender]=0
            sender_word_count_dict[sender]+=len(message.split(" "))
        max_value=max(sender_word_count_dict.values())
        final_sender=""
        #print(sender_word_count_dict)
        for key,value in sender_word_count_dict.items():
            if value==max_value and key>final_sender:
                final_sender=key
        return final_sender