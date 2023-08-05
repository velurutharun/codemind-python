class Solution:
    def decompressRLElist(self, nums):
        count = 0
        for i in range(0, len(nums), 2):
            count += nums[i]

        idx = 0
        ans = [0] * count

        for i in range(1, len(nums), 2):
            freq = nums[i - 1]
            val = nums[i]
            while freq > 0:
                ans[idx] = val
                idx += 1
                freq -= 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    # Taking user input for the nums array
    n = int(input())
    nums = list(map(int,input().split()))
    # Call the decompressRLElist function with the user-provided nums array
    result = solution.decompressRLElist(nums)

    # Print the result
    print(*result)
