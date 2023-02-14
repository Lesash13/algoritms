# ID = 81963873
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1