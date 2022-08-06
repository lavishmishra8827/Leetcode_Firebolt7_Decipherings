class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        daynow=0
        taskdict={}
        for i in tasks:
            if i not in taskdict or daynow-taskdict[i]>=space:
                daynow+=1
            else:
                daynow=taskdict[i]+space+1
            taskdict[i]=daynow
        return daynow