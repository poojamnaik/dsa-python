# Reverse String

## Problem

Given a string `A`, reverse the string and return the reversed string.

## Approach

Traverse the string from right to left.

For every character:

1. Add the character to a list.
2. After all characters have been processed, use `join()` to construct the reversed string.

For example:

```text
A = "hello"

Traversal:
o → l → l → e → h

Result:
"olleh"



### Local testing

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("hello", "olleh"),
        ("abc", "cba"),
        ("a", "a"),
        ("python", "nohtyp"),
    ]

    for A, expected in test_cases:
        result = solution.solve(A)
        print(f"A = {A}, Output = {result}, Expected = {expected}")