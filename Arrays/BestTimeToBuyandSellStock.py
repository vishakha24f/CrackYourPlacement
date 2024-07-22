class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count=0
        min= float('inf')
        for i in prices:
            if i<min:
                min= i
            elif i-min>count:
                count= i-min
        return count
        