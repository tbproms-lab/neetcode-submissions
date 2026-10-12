class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        correct = [x for x in range(0, len(nums)+1)]
        nums.sort()
        answer = 0
        
        for i in range(len(correct)):
            if i == len(nums):
                answer = correct[i]
                break
            if correct[i] != nums[i]:
                answer = correct[i]
                break
            continue
        
        return answer
        
