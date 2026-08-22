# String Operations

## Problem

Given a string `A` containing lowercase and uppercase alphabets, perform the following operations in order:

1. Concatenate the string with itself.
2. Delete all uppercase letters.
3. Replace every lowercase vowel with `#`.

Return the resultant string.

## Approach

Since both copies of `A` undergo exactly the same transformations, we can avoid explicitly creating `A + A`.

Instead:

1. Traverse `A` once.
2. Ignore uppercase characters.
3. Replace lowercase vowels with `#`.
4. Keep other lowercase characters unchanged.
5. Duplicate the transformed result.

For example:

```text
A = "Abca"

Transform:
A → ignored
b → b
c → c
a → #

First transformed copy:
"bc#"

After concatenating with itself:
"bc#bc#"

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("Abca", "bc#bc#"),
        ("aAbB", "#b#b"),
        ("HELLO", ""),
        ("abc", "#b c#".replace(" ", "")),
        ("xyz", "xyzxyz"),
    ]

    for A, expected in test_cases:
        result = solution.solve(A)
        print(f"A = {A}, Output = {result}, Expected = {expected}")