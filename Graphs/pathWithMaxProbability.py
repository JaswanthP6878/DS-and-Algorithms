'''
1514. Path with Maximum Probability
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
'''


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        '''
        we create a defaultdict which is a adjacency list 
        '''
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst,succProb[i]])
            adj[dst].append((src, succProb[i]))

        pq = [(-1, start)] #as python does not have a MaxHeap we create a min heap with negitive values
        visited = set()


        # we perform dijkstra but as we take a max heap we get the max probabilities
        # on every iteration
        while pq:
            prob, curr =  heapq.heappop(pq)
            visited.add(curr)
            if curr == end:
                return -1*prob
            else :
                for nei, edgeprob in adj[curr]:
                    if nei not in visited:
                        heapq.heappush(pq, (prob * edgeprob, nei))
        return 0
