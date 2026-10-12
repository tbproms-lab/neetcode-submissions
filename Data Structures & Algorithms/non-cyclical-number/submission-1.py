class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()

        while True:
            total = 0
            n = str(n)
            for x in n:
                total += int(x) ** 2
            if total == 1:
                return True
            if total in store:
                break
            store.add(total)
            n = total

        return False

