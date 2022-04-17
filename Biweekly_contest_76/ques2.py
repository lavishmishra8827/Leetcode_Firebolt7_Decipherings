class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        max_pens=total//cost1
        ways=0
        for pen_taken in range(max_pens+1):
            ways+=((total-pen_taken*cost1)//cost2)+1
        return ways