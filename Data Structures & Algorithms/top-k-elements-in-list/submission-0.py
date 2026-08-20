class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num,0)
        freq = []
        for item, count in hashMap.items():
            freq.append([count,item])
        freq.sort()
        result = []
        for i in range(1,k+1):
            result.append(freq.pop()[1])
        return result
