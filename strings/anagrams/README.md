# Anagrams

## Problem

Given two lowercase strings `A` and `B` of length `N`, return `1` if they are anagrams of each other, otherwise return `0`.

Two strings are anagrams if one can be formed by rearranging the characters of the other.

## Approach

Since the strings contain only lowercase English letters, there are only 26 possible characters.

Use a frequency array of size 26.

1. For every character in `A`, increment its frequency.
2. For every character in `B`, decrement its frequency.
3. If all frequencies are `0`, the strings contain exactly the same characters with the same frequencies.
4. Otherwise, they are not anagrams.

The character index is calculated using:

```text
index = ord(character) - ord('a')


# Testing
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("listen", "silent", 1),
        ("hello", "world", 0),
        ("a", "a", 1),
        ("a", "b", 0),
        ("z", "z", 1),
        ("z", "a", 0),
        ("abb", "bab", 1),
    ]

    for A, B, expected in test_cases:
        result = solution.solve(A, B)
        print(f"A = {A}, B = {B}, Output = {result}, Expected = {expected}")