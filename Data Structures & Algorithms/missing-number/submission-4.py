class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #correct = [x for x in range(0, len(nums)+1)]
        nums.sort()
        answer = 0
        
        for i in range(len(nums)+ 1):
            if i == len(nums):
                answer = i
                break
            if i != nums[i]:
                answer = i
                break
            continue
        
        return answer
        
