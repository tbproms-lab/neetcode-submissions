class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        oop = set(nums)

        h1 = dict()
        
        for num in oop:
            h1[num] = 0

        for x in nums:
            h1[x] += 1

        zipped = list(zip(h1.keys(),h1.values()))

        maxl = []

        for item in zipped:
            maxl.append(item[1])
        
        maxl = sorted(maxl)
        maxl.reverse()

        print(maxl)

        answer = []

        for amount in range(k):
            for item in zipped:
                if item[1] == maxl[amount]:
                    answer.append(item[0])

        return list(set(answer))


