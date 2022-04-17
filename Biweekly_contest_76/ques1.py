class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mindistance=100001
        number=nums[0]
        for i in nums:
            distance_now=abs(i)
            if distance_now<=mindistance:
                if i<0 and distance_now==mindistance:
                    continue
                number=i
                mindistance=distance_now
        return number