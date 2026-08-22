class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        maxPotential = 0
        totalOnes = 0
        N= len(A)
        for i in range(N):
            if(A[i] == '1'):
                totalOnes = totalOnes+1
        
        if(totalOnes == 0):
            return 0
        if(totalOnes == N):
            return N

        for i in range(N):
            
            if(A[i] == '0'):
                left = 0
                right =0
                j=i-1
                k= i+1
                while(j>=0 and A[j] == '1' ):
                    j = j-1
                    left = left+1
                while(k<N and A[k] == '1' ):
                    k = k+1
                    right = right+1
                

                maxPotential = max(maxPotential, min(right+left+1,totalOnes))
        return maxPotential
            