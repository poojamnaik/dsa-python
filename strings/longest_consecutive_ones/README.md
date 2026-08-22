# Longest Consecutive Ones After One Swap

## Problem

Given a binary string `A`, perform at most one swap between a `0` and a `1` to maximize the length of consecutive `1`s.
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.

## Approach

Count the total number of `1`s first.

Then traverse the string and consider each `0` as the position where a `1` could be swapped in.

For each `0`, calculate:

- consecutive `1`s immediately to its left
- consecutive `1`s immediately to its right
- one additional `1` obtained by the swap

The potential length is:

`left + right + 1`

However, the result cannot exceed the total number of `1`s in the string.

The traversal processes each character only once.

## Complexity

- Time: `O(N)`
- Space: `O(1)`