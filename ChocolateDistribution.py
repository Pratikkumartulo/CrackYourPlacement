class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A = sorted(A)
        mini = float('inf')
        for i in range(N-M+1):
            mini=min(mini,A[i+M-1]-A[i])
        return mini