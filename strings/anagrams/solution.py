# Time: O(N) | Space: O(1)
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def solve(self, A, B):
        frequencies = [0] * 26

        for ch in A:
            index = ord(ch) - ord('a')
            frequencies[index] += 1

        for ch in B:
            index = ord(ch) - ord('a')
            frequencies[index] -= 1

        for i in range(26):
            if frequencies[i] != 0:
                return 0

        return 1
