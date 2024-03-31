#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict


def log_parsing():
    """function that reads stdin line by line and computes metrics"""
    total_file_size = 0
    count_status_code = defaultdict(int)
    code_array = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for i, line in enumerate(sys.stdin, start=1):
            line_args = line.strip()
            line_args = re.split(r'\s+|-', line_args)
            line_args = [arg for arg in line_args if arg]
            if len(line_args) != 10:
                continue
            status_code = line_args[8]
            file_size = line_args[9]
            total_file_size += int(file_size)
            if not status_code.isdigit():
                continue
            count_status_code[int(status_code)] += 1
            if i % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(count_status_code.keys()):
                    if code not in code_array:
                        continue
                    print(f"{code}: {count_status_code[code]}")
    except KeyboardInterrupt:
        pass
    print(f"File size: {total_file_size}")
    for code in sorted(count_status_code.keys()):
        if code not in code_array:
            continue
        print(f"{code}: {count_status_code[code]}")


log_parsing()
