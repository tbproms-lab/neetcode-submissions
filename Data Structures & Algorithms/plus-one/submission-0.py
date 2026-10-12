class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""

        for x in digits:
            num += str(x)

        new = str(int(num) + 1)

        lyst = []

        for x in new:
            lyst.append(x)

        return lyst


