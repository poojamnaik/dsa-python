# Reverse Words in a String

## Problem

Given a string `A`, reverse the string word by word.

A word is a sequence of non-space characters.

The result must:

- Have the words in reverse order.
- Have no leading or trailing spaces.
- Have exactly one space between words.

## Example

### Input

```text
"  this   world is beautiful  "


Output
"beautiful is world this"

Approach

Instead of using Python's built-in split(), reverse(), or join() functions, traverse the string from right to left.

Skip spaces.
Mark the end of a word.
Continue moving left until the beginning of the word is found.
Add the word to the result.
Repeat until the beginning of the string is reached.
Add a single space between words.

Traversing from right to left naturally produces the words in reverse order, so no separate reversal operation is required.

Complexity
Time: O(N)
Space: O(N)