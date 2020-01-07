class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        max = A[0]
        maxIndex = 0
        c = []

        for i in range(B):
            if ( A[i] > A[maxIndex]):
                maxIndex = i
        
        c.append(A[maxIndex])

        for i in range(B, len(A)):
            if (maxIndex + B) > i:
                if A[i] >= A[maxIndex]:
                    maxIndex = i
                
            else:
                maxIndex = i-(B-1)
                for j in range(i-(B-1), i+1):
                    if ( A[j] >= A[maxIndex]):
                        maxIndex = j
            
            c.append(A[maxIndex])
        
        return c