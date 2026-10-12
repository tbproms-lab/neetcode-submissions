class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] + c < 10:
                digits[i] = digits[i] + c
                c = 0
            else:
                digits[i] = 0
                c = 1

        if c==1:
            digits.insert(0,c)

        return digits


