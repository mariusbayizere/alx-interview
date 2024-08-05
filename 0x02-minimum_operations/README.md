# 0x02. Minimum Operations

## Description
This project involves calculating the minimum number of operations needed to achieve exactly `n` characters of 'H' in a text file. The only operations allowed are "Copy All" and "Paste". The goal is to determine the fewest number of operations required to reach the specified number of characters.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Minimum Operations
**Mandatory**

In a text file, there is a single character 'H'. The text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

- **Prototype:** `def minOperations(n)`
- **Returns:** an integer
- If `n` is impossible to achieve, return `0`

**Example:**
