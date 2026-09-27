class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper = len(nums) - 1

        lower = 0

        while lower <= upper:
            index = (lower+upper)//2
            if target < nums[index]:
                upper = index - 1
            elif target > nums[index]:
                lower = index + 1
            elif target == nums[index]:
                return index

        return -1
