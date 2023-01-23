'''
    347. Top K Frequent Elements leetcode
    Given an integer array nums and an integer k, 
    return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = dict()
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else :
                hm[i] += 1
        counts = []
        for i in hm.values():
            counts.append(i)
        out = []
        counts.sort(reverse = True)
        counts_k = []
        j = 0
        while(k > 0):
            counts_k.append(counts[j])
            j += 1
            k -= 1
        j = 0
        for i,v in hm.items():
            if(v in counts_k):
                out.append(i)
        return out



