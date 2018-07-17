# Given a matrix A, return the transpose of A.
# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.
#Example 1:
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

# 36 / 36 test cases passed.
# Status: Accepted
# Runtime: 60 ms

# You are here!
# Your runtime beats 99.13 % of python3 submissions.

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0:
            return []
        B = []
        for j in range(len(A[0])):
            temp = []
            for i in A:
                temp.append(i[j])
            B.append(temp)
        return B

A = [[1,2,3],
     [4,5,5],
     [7,8,9]]
s = Solution()
res = s.transpose(A)
print(res)