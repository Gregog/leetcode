class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_elements = len(nums)
        result = []
        for i in range(num_elements - 1):
            for j in range(i + 1, num_elements):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
            if len(result) > 0:
                break
        return result
