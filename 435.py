class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """ Be greedy on the end times of the lectures """
        if len(intervals) == 0: return 0
        # Use sorted function to sort intervals based on the s
        sortedList = sorted(intervals, key=lambda x: x[1]) 
        currEndTm = sortedList[0][1]
        intvs = sortedList[1:]
        numInc = 1 # Intervals to include in final answer
        for intv in intvs:
            if intv[0] >= currEndTm: numInc += 1; currEndTm = intv[1]
        return len(intervals) - numInc
        

if __name__ == "__main__":
    intvs = [[1,100],[11,22],[1,11],[2,12]]
    sol = Solution()
    print(sol.eraseOverlapIntervals(intvs))


