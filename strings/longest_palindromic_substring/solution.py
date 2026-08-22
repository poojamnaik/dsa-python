# Time: O(N^2) | Space: O(1)
class Solution:
    # @param A : string
    # @return a string

    def longestPalindrome(self, A):

        if len(A) == 1:
            return A

        maxPalindrome = A[0]

        for i in range(1, len(A)):

            # Odd-length palindrome
            oddPalindrome = self.checkPalindromeSubstring(A, i - 1, i + 1)

            if len(oddPalindrome) > len(maxPalindrome):
                maxPalindrome = oddPalindrome

            # Even-length palindrome
            evenPalindrome = self.checkPalindromeSubstring(A, i - 1, i)

            if len(evenPalindrome) > len(maxPalindrome):
                maxPalindrome = evenPalindrome

        return maxPalindrome

    def checkPalindromeSubstring(self, A, si, ei):

        while si >= 0 and ei < len(A) and A[si] == A[ei]:
            si -= 1
            ei += 1

        return A[si + 1:ei]