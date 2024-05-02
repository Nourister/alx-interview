#!/usr/bin/python3

import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print("Total file size:", total_size)
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

status_codes = {}
total_size = 0
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue
        ip_address, date, method, status_code, file_size = parts[0], parts[3][1:], parts[5], parts[6], int(parts[7])
        if not status_code.isdigit():
            continue
        status_code = int(status_code)
        if status_code not in status_codes:
            status_codes[status_code] = 0
        status_codes[status_code] += 1
        total_size += file_size
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    signal_handler(signal.SIGINT, None)
