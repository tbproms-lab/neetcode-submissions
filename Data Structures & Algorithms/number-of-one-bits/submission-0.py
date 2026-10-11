class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""

        while n > 0:
            rem = n % 2
            binary = str(rem) + binary
            n = n//2

        one = 0

        for x in binary:
            if x == str(1):
                one += 1

        return one