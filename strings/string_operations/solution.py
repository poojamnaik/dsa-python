# Time: O(N) | Space: O(N)
class Solution:
    # @param A : string
    # @return a string

    def solve(self, A):

        arr = []

        for ch in A:

            if ch in ['a', 'e', 'i', 'o', 'u']:
                arr.append('#')

            elif ord(ch) < 65 or ord(ch) > 90:
                arr.append(ch)

        n = len(arr)

        for i in range(n):
            arr.append(arr[i])

        return "".join(arr)