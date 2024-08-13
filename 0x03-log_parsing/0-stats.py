#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics."""

import sys


def display_metrics(status_counts, total_file_size):
    """Displays the collected metrics."""
    print("File size: {:d}".format(total_file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] != 0:
            print("{}: {:d}".format(status_code, status_counts[status_code]))


def main():
    """Main function to parse input and compute metrics."""
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0
    }
    line_count = 0
    total_file_size = 0

    try:
        for log_line in sys.stdin:
            if line_count != 0 and line_count % 10 == 0:
                display_metrics(status_counts, total_file_size)

            log_parts = log_line.split()
            line_count += 1

            try:
                total_file_size += int(log_parts[-1])
            except ValueError:
                pass

            try:
                if log_parts[-2] in status_counts:
                    status_counts[log_parts[-2]] += 1
            except IndexError:
                pass

        display_metrics(status_counts, total_file_size)

    except KeyboardInterrupt:
        display_metrics(status_counts, total_file_size)
        raise


if __name__ == "__main__":
    main()
