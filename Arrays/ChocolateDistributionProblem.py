class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        mindiff = A[N-1]-A[0]
        for i in range (0, N-M+1):
            mindiff= min(mindiff, (A[i+M-1]-A[i]))
        return mindiff
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())
        solObj = Solution()
        print(solObj.findMinDiff(A,N,M))
