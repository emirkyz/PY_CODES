from typing import List
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):  # 1
            remaining = target - nums[i]  # 2

            if remaining in seen:  # 3
                return [i, seen[remaining]]  # 4
            else:
                seen[value] = i  # 5
            print(seen)


a = Solution()
print(a.twoSum([2, 3, 1], 3))

araba = np.zeros((2, 3))
print(araba)
print("hello world")
print(np.array(3213.2))
