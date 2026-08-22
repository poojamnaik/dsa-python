# Time: O(N) | Space: O(N)
class Solution:

    # @param A : string
    # @return a strings

    def solve(self, A):

        arr = []

        for i in range(len(A)-1, -1, -1):
            arr.append(A[i])

        return "".join(arr)