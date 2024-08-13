Log Parsing
Overview
This project consists of a Python script that reads log data from standard input (stdin) and computes metrics based on the log entries. The log entries should follow a specific format, and the script will compute statistics such as total file size and the number of occurrences of specific status codes.

The project includes two Python scripts:

0-generator.py: A script that generates random log data.
0-stats.py: A script that reads log data from stdin and prints statistics.
Requirements
Allowed editors: vi, vim, emacs
Python version: 3.4.3 (Python 3.4 or later)
Files must end with a newline
Files must start with the shebang line: #!/usr/bin/python3
Code must follow PEP 8 style (version 1.7.x)
All files must be executable
The length of files will be tested using wc (word count)
Tasks
0. Log Parsing
Mandatory

Write a script that reads stdin line by line and computes metrics as follows:

Input format:

php
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(Lines not matching this format will be skipped.)

Statistics to compute:

Total file size: The sum of all <file size> values.
Number of lines by status code:
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
Status codes should be printed in ascending order.
If a status code doesn’t appear or is not an integer, don’t print anything for that status code.
Output format:

After every 10 lines and/or a keyboard interruption (CTRL + C), print:
arduino
Copy code
File size: <total size>
<status code>: <number>
where <total size> is the sum of all previous file sizes, and <status code>: <number> indicates the number of occurrences of each status code.
Example:

yaml
Copy code
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
Usage
Generate Random Log Data:

bash
Copy code
./0-generator.py
Compute and Print Metrics:

bash
Copy code
./0-generator.py | ./0-stats.py
Implementation Details
0-generator.py: Generates random log data with the format required for the metrics script.
0-stats.py: Reads log data from stdin, computes metrics, and prints the results.
Repository
GitHub repository: alx-interview
Directory: 0x03-log_parsing
File: 0-stats.py
Feel free to modify the README as needed to better fit the specifics of your project or any additional requirements.
