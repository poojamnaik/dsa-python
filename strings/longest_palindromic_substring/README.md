# Longest Palindromic Substring

## Problem

Given a string `A`, find and return the longest palindromic substring.

If multiple palindromic substrings have the same maximum length, return the one that occurs first.

## Approach

Use the **expand around center** technique.

A palindrome can have two types of centers:

- Odd-length palindrome: one character is the center.
- Even-length palindrome: two characters are the center.

For every position `i`, check both:

```text
Odd:  (i - 1, i + 1)
Even: (i - 1, i)

Example:

Input:
A = "babad"

Output:
"bab"