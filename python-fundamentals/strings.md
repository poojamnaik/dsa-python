# Python Strings for DSA


A practical reference for Python string concepts used in Data Structures
and Algorithms problems.


---


## 1. Creating Strings


A string is a sequence of Unicode characters.


```python
s = "hello"
```

Strings can use single or double quotes:

```
s1 = "hello"
s2 = 'hello'
```


## 2. String Indexing

Python uses zero-based indexing.
```
s = "hello"


s[0]   # 'h'
s[1]   # 'e'
s[-1]  # 'o'
s[-2]  # 'l'
```

Index representation:
```
       h   e   l   l   o
       0   1   2   3   4
      -5  -4  -3  -2  -1
```
DSA

Use indexing when a problem requires access to a specific position:
```
if s[i] == s[i - 1]:
    ...
```

## 3. Iterating Over a String

Character only

Use this when the index is not required:
```
for ch in s:
    print(ch)
```

Index + character
```
for i in range(len(s)):
    print(i, s[i])
```

A more Pythonic alternative:

```
for i, ch in enumerate(s):
    print(i, ch)
```
Reverse traversal
```
for i in range(len(s) - 1, -1, -1):
    print(s[i])
```

For a string of length 5:
```
range(4, -1, -1)
```

produces:
```

4, 3, 2, 1, 0
```

Remember that the stop value is exclusive.

## 4. String Slicing

Syntax:
```

s[start:stop:step]
```

Rules:

start is inclusive
stop is exclusive
step determines the direction and jump size

Example:
```
s = "abcdef"


s[1:4]    # "bcd"
s[:3]     # "abc"
s[3:]     # "def"
s[:]      # "abcdef"
```
Step
```
s[::2]    # "ace"
```

Indexes:
```
0 → 2 → 4
a → c → e
```

Reverse
```
s[::-1]   # "fedcba"
```

Negative indexes
```
s[-1]     # last character
s[-2]     # second-last character
s[-3:]    # last 3 characters
```

Reverse slicing
```
s = "abcdefgh"

s[7:2:-1]     # "hgfed"
s[5:0:-2]     # "fdb"
s[-1:-5:-1]   # "hgfe"
```

The stop index is still excluded even when moving backwards.

Complexity

Slicing creates a new string.

For a slice containing k characters:

Time: O(k)
Space: O(k)

Be careful about creating large slices repeatedly inside loops, as this can lead to O(n²) total work.

## 5. String Immutability

Python strings are immutable.

This is not allowed:

```
s = "hello"
s[0] = "H"
```

It raises:
```
TypeError: 'str' object does not support item assignment
```

An existing string object cannot be modified.

### Reassignment is different from mutation

This is valid:
```
s = "hello"
s = "Hello"
```

The original "hello" string was not modified.

The variable s was simply reassigned to another string object.

### Multiple references
```
s = "hello"
t = s
```

Both variables refer to the same string object.
```
s ─────┐
       ├──> "hello"
t ─────┘
```

Because strings are immutable, neither variable can modify the string.

### Important distinction
#### Mutation

Modify an existing object:
```
s[0] = "H"
```

Not possible for strings.

#### Reassignment

Change what a variable refers to:
```
s = "Hello"
```

Valid.

#### Multiple references
```
s = "hello"
t = s
```

Both refer to the same object.

## 6. Building Strings

Because strings are immutable, use a list when constructing a string incrementally.
```
chars = []
for ch in s:
    chars.append(ch)

result = "".join(chars)
```

Example:
```
s = "hello"

chars = []

for ch in s:
    chars.append(ch.upper())

result = "".join(chars) # "HELLO"
```

#### Why use a list?

Lists are mutable:
```
chars.append("a")
chars.append("b")
```

Then construct the final immutable string once:
```
"".join(chars)
```
This is similar in purpose to Javas StringBuilder pattern.

#### Complexity

For n characters:

Traversal: O(n)
Appending: O(1) amortized per operation
join(): O(n)
Total: O(n)
Extra space: O(n)

#### Important

Do not assume that every use of + is bad.

This is perfectly reasonable:
```
result = "Hello " + name
```

The list + join() pattern is especially useful when repeatedly building a string inside a loop.

## 7. split()

split() converts a string into a list of strings.
```
s = "hello world"

words = s.split() # ["hello", "world"]
```

#### split() with no argument
```
s = "  the   sky   is blue  "
s.split()
```

Result:
```
["the", "sky", "is", "blue"]
```

It:

    removes leading whitespace
    removes trailing whitespace
    treats consecutive whitespace as separators
    does not produce empty strings for consecutive whitespace

#### split(" ") is different
```
s = "  the   sky  "
s.split(" ")
```

can produce empty strings:
```
["", "", "the", "", "", "sky", "", ""]
```

Use:
```
s.split()
```

when you want to split text into words while ignoring arbitrary whitespace.

## 8. join()

join() combines strings into one string.
```
words = ["the", "sky", "is", "blue"]
result = " ".join(words)
```

Result:
```
"the sky is blue"
```

The object before .join() is the separator.
```
"-".join(words) # "the-sky-is-blue"
"".join(words) # "theskyisblue"
```

split() and join()

They are conceptually opposites:
```
"the sky is blue"
        ↓ split()
["the", "sky", "is", "blue"]
        ↓ join()
"the sky is blue"
```

## 9. strip()

strip() removes whitespace from both ends of a string.
```
s = "   hello world   "
s.strip() # "hello world"
```

Related methods:
```
s.strip()     # both sides
s.lstrip()    # left side
s.rstrip()    # right side
```

strip() does not remove whitespace from the middle:
```
"hello   world".strip() # "hello   world"
```

## 10. replace()

replace() creates a new string with replacements.
```
s = "hello world"
result = s.replace("world", "Python") # "hello Python"
```

Strings remain immutable; replace() returns a new string.

## 11. Whitespace Normalization Pattern

A very useful pattern:
```
s = "hello   world"
result = " ".join(s.split())
```

Result:
```
"hello world"
```

Process:
```
"hello   world"
       ↓ split()
["hello", "world"]
       ↓ " ".join()
"hello world"
```
This is particularly useful when a problem says:

remove leading spaces
remove trailing spaces
reduce multiple spaces to one
## 12. ord() and chr()

Python characters have Unicode code points.

ord()

Converts a character to its numeric code.
```
ord('a')   # 97
ord('b')   # 98
ord('A')   # 65
ord('C')   # 67
```

chr()

Converts a numeric code back to a character.
```
chr(97)    # 'a'
chr(65)    # 'A'
```

Conceptually:
```
'a' ──ord()──> 97
'a' <──chr()── 97
```

## 13. Character → Array Index

For lowercase English letters:
```
index = ord(ch) - ord('a')
```

This maps:
```
a → 0
b → 1
c → 2
...
z → 25
```

Example:
```
ch = 'm'
index = ord(ch) - ord('a') # 12
```

Reverse mapping:
```
ch = chr(index + ord('a'))
```
Important

This technique assumes the input contains lowercase English letters.

Do not blindly use:
```
ord(ch) - ord('a')
```

if ch could be uppercase, a digit, punctuation, or arbitrary Unicode.

## 14. Character Frequency Array

When the problem guarantees lowercase English letters, we can use an array of size 26 instead of a dictionary.
```
frequency = [0] * 26
for ch in s:
    index = ord(ch) - ord('a')
    frequency[index] += 1
```

For:
```
s = "apple"
```

the character 'p' maps to:
```
ord('p') - ord('a') #15
```

So:
```
frequency[15]
```
stores the frequency of 'p'.

#### Complexity

For a string of length n:

Time: O(n)
Space: O(1)

Why O(1) space?

Because the array always contains exactly 26 elements regardless of input size.

## Quick Reference


| Operation    | Example                     | Purpose                |
| ------------ | --------------------------- | ---------------------- |
| Index        | `s[i]`                      | Access character       |
| Length       | `len(s)`                    | Number of characters   |
| Iterate      | `for ch in s`               | Character traversal    |
| Enumerate    | `for i, ch in enumerate(s)` | Index + character      |
| Reverse loop | `range(len(s)-1,-1,-1)`     | Backward traversal     |
| Slice        | `s[1:4]`                    | Extract substring      |
| Reverse      | `s[::-1]`                   | Create reversed string |
| Split        | `s.split()`                 | String → list          |
| Join         | `" ".join(words)`           | List → string          |
| Strip        | `s.strip()`                 | Remove edge whitespace |
| Replace      | `s.replace(a,b)`            | Replace substring      |
| Ord          | `ord('a')`                  | Character → number     |
| Chr          | `chr(97)`                   | Number → character     |

## DSA Patterns to Remember

### Character traversal
```
for ch in s:
    ...
```

### Index traversal
```
for i in range(len(s)):
    ...
```

### Index + character
```
for i, ch in enumerate(s):
    ...
```

### Reverse traversal
```
for i in range(len(s) - 1, -1, -1):
    ...
```

### Build a string
```
result = []
for ch in s:
    result.append(ch)
return "".join(result)
```

### Normalize whitespace
```
" ".join(s.split())
```

### Lowercase frequency array
```
frequency = [0] * 26
for ch in s:
    frequency[ord(ch) - ord('a')] += 1
```

Python vs Java — DSA Mental Model
| Java                | Python               |
| ------------------- | -------------------- |
| `String`            | `str`                |
| String immutable    | String immutable     |
| `StringBuilder`     | `list` + `"".join()` |
| `charAt(i)`         | `s[i]`               |
| `s.length()`        | `len(s)`             |
| `substring()`       | slicing `s[a:b]`     |
| `split()`           | `split()`            |
| `String.join()`     | `" ".join()`         |
| character → numeric | `ord(ch)`            |
| numeric → character | `chr(n)`             |


## Key Takeaways

Before solving string DSA problems, remember:

1. Strings are immutable.
2. s[i] accesses a character.
3. s[start:stop] has an exclusive stop.
4. s[::-1] creates a reversed copy.
5. Use enumerate() when you need both index and character.
6. Use split() for word-based processing.
7. Use " ".join(...) to construct a string with separators.
8. Use list + join() when building strings incrementally.
9. ord() converts a character to a numeric code.
10. chr() converts a numeric code to a character.
11. ord(ch) - ord('a') maps lowercase letters to 0–25.
12. A 26-element frequency array gives O(1) auxiliary space for lowercase English letters.
13. Always consider the time and space cost of slicing.


## Common Interview Traps
1. Strings cannot be modified
```s[0] = 'H'       # ❌``````
2. stop in slicing is exclusive
``` s[1:4]```
uses indexes:
```1, 2, 3```
not 4.
3. split() and split(" ") are different
```
    s.split()        # whitespace-aware
    s.split(" ")     # literal space
```
4. Slicing creates a new string
```s[::-1]  ```
is O(n) time and O(n) space.

5. Dont blindly use ord(ch) - ord('a')

Only use it when the character range is known, such as lowercase English letters.

6. Reassignment is not mutation
```
s = "hello"
s = "Hello"
```

does not modify "hello".

indexing, iteration, range(), and reverse traversal. 

| Situation                  | Pattern                                                   |
| -------------------------- | --------------------------------------------------------------|
| Need only characters       | `for ch in s:`                                                |
| Need index + character     | `for i in range(len(s)):` `or i, ch in enumerate(s)`          |
| Need to traverse backwards | `for i in range(len(s)-1, -1, -1):`                           |
| Need to traverse backwards | `for i in range(len(s)-1, -1, -1):`                           |

