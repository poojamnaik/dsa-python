# Complexity - Time: O(N) | Space: O(N)
class SolutionMain:
    # @param A : string
    # @return a strings
    def solve(self, A):
        arr = []
        startIndex = 0

        for i in range(len(A)):
            
            if(i!=0 and A[i] == ' 'and A[i-1]!= ' '):
                    arr.append(A[startIndex:i])

            elif(i!=0 and A[i-1] == ' ' and  A[i]!= ' '):
                    startIndex = i

       
        return " ".join(arr[::-1])
    
class Solution1:
    # @param A : string
    # @return a strings
    def solve(self, A):

        arr = []
        startIndex = 0

        for i in range(len(A)):

            # End of a word
            if A[i] == ' ':
                if i != 0 and A[i - 1] != ' ':
                    arr.append(A[startIndex:i])

            # Start of a new word
            elif i != 0 and A[i - 1] == ' ':
                startIndex = i

        # Add the last word if the string doesn't end with a space
        if len(A) > 0 and A[-1] != ' ':
            arr.append(A[startIndex:])

        return " ".join(arr[::-1])

class Solution2:
    # @param A : string
    # @return a string

    def solve(self, A):
        result = ""
        i = len(A) - 1

        while i >= 0:

            # Skip spaces
            while i >= 0 and A[i] == ' ':
                i -= 1

            if i < 0:
                break

            # Find the end of the current word
            end = i

            # Find the beginning of the current word
            while i >= 0 and A[i] != ' ':
                i -= 1

            start = i + 1

            # Add a single space between words
            if result != "":
                result += " "

            result += A[start:end + 1]

        return result
