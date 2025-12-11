
This repository contains a script for calculating prime factors of a string via a bijection between ASCII strings and numbers.

For a given string we describe the bijection:

All string characters are converted to HEX via ASCII.
Then, the HEX values are concatenated into a new value.
This new value is the numeric representation of the string.

The string can be reconstructed from the numeric representation by interpreting each byte as an ASCII value.

# How to use

```bash
$ python3 main.py <short text>
```


# Example

```bash
$ python3 main.py "GitHub"
2 * 3 * 101 * 991 * 130744769

# check if this is true
$ python3 -c "print((2 * 3 * 101 * 991 * 130744769).to_bytes(6, 'big'))"
b'GitHub'
```


