class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dpt = [False]*len(nums); dpt[-1] = True # Initalize dp table
        sqrs = nums[:-1]
        target = len(sqrs)
        for i, maxJmp in reversed(list(enumerate(sqrs))):
            for jmp in range(1,maxJmp+1):
                if i+jmp <= target and dpt[i+jmp]:
                    dpt[i] = True
                    break
        return dpt[0]



if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))

    sol = Solution()
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))



# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.