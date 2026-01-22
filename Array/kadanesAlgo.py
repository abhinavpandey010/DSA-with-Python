class Solution:
    def maxSubarraySum(self, arr):
        curr = arr[0]
        best = arr[0]

        for i in range(1, len(arr)):
            curr = max(arr[i], curr + arr[i])
            best = max(best, curr)

        return best


if __name__ == "__main__":
    # Example input
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    sol = Solution()
    result = sol.maxSubarraySum(arr)

    print("Maximum Subarray Sum:", result)
