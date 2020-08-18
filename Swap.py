class Solution(object):
    def canTransform(self, start, end):
        i, j = 0, 0
        N = len(start)
        while i < N and j < N:
            while i < N - 1 and start[i] == 'X':
                i += 1
            while j < N - 1 and end[j] == 'X':
                j += 1
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True
val=Solution()
start,end=map(str,input().split())
print(val.canTransform(start,end))
