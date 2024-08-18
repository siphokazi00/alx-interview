#!/usr/bin/env python3
"""
This script reads lines from stdin and computes metrics.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the computed statistics.
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line, total_size, status_codes):
    """
    Processes a single line of input and updates metrics.
    """
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

    except (IndexError, ValueError):
        # Skip the line if it doesn't match the expected format
        pass

    return total_size, status_codes


def main():
    """
    Entry point
    """
    total_size = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = process_line(line.strip(),
                                                    total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
