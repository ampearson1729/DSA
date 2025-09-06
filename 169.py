from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        numTmsAppeared = defaultdict(int)
        maxAppd = 0; maxNum = None
        for x in nums:
            numTmsAppeared[x] += 1
            xApp = numTmsAppeared[x]
            if xApp > maxAppd: maxNum, maxAppd = x, xApp
        return maxNum


if __name__ == "__main__":
    nums = [3,2,3]
    sol = Solution()
    print(sol.majorityElement(nums))

    nums = [2,2,1,1,1,2,2]
    sol = Solution()
    print(sol.majorityElement(nums))

