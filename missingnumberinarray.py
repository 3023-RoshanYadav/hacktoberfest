class Solution:
    def MissingNumber(self,array,n):
        actual=sum(array)
        expected=n*(n+1)/2
        return int(expected-actual)
