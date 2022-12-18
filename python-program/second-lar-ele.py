class Solution:

    def print2largest(self,arr, n):
        max = arr[0]
        second = -1
        for i in range(n):
            if arr[i]>max:
                second = max
                max = arr[i]
            elif arr[i]>second and arr[i]<max:
                second = arr[i]
        return second