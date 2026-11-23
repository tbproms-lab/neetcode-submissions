class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 1
        lyst = []

        nums = sorted(list(set(nums)))
        leng = len(nums)

        for n in range(leng):
            try:
                if nums[n] == (nums[n+1] - 1):
                    longest += 1
                else:
                    longest = 1
                lyst.append(longest)

            except IndexError:
                lyst.append(longest)

        return max(lyst) if len(lyst) > 0 else 0