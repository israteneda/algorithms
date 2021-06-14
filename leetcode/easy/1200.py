"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""

from typing import List

class Solution:
    def minimum_abs_difference(self, arr: List[int]) -> List[List[int]]:
        res = list()
        sorted_arr = sorted(arr)
        min_difference = self.get_min_difference(arr)
        for i in range(len(sorted_arr), 2):
        
        return res


    def get_min_difference(self, arr: List[int]) -> int:
        min_difference = max(arr)
        for n in arr:
            for m in arr:
                if n != m:
                    difference = abs(m - n)
                    if difference < min_difference:
                        min_difference = difference
        
        return min_difference

solution = Solution()
print(solution.minimum_abs_difference([4,2,1,3]))
print(solution.minimum_abs_difference([1,3,6,10,15]))
print(solution.minimum_abs_difference([3,8,-10,23,19,-4,-14,27]))
