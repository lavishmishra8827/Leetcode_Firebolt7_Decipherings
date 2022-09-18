class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        number_of_days=[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        a_start_month,a_start_day=list(map(int,arriveAlice.split("-")))
        a_end_month,a_end_day=list(map(int,leaveAlice.split("-")))
        b_start_month,b_start_day=list(map(int,arriveBob.split("-")))
        b_end_month,b_end_day=list(map(int,leaveBob.split("-")))
        alice_set=set()
        def make_days_set(start_day,start_month,end_day,end_month):
            #print(start_day,start_month,end_day,end_month)
            day=start_day
            month=start_month
            givenset=set()
            while(True):
                #print(day,month)
                givenset.add(str(day)+"-"+str(month))
                if day==end_day and month==end_month:
                    return givenset
                day+=1
                if day>number_of_days[month]:
                    day=1
                    month+=1
            return givenset
        alice_set=make_days_set(a_start_day,a_start_month,a_end_day,a_end_month)
        bob_set=make_days_set(b_start_day,b_start_month,b_end_day,b_end_month)
        #print(alice_set)
        #print(bob_set)
        return len(alice_set.intersection(bob_set))
                