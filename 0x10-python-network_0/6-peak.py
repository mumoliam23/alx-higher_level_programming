#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def search(nums, left, right):

    if left == right:
        return nums[left]
    mid = int((left + right) / 2)
    if nums[mid] >= nums[mid + 1]:
        return search(nums, left, mid)
    return search(nums, mid+1, right)


def find_peak(list_of_integers):
    """
        - Brute force algorith will lead to O(nlog(n)),
        we will just sort the array and find the maximum

        - Better approach is to use binary search.

        if the active value is greater than the next,
        then the peak is in the left part of the list

        if not, the peak is in the second part
        we stop when the left and right index are the same

        complexity: O(log(n))
    """
    if not list_of_integers:
        return None
    return search(list_of_integers, 0, len(list_of_integers) - 1)
