# Log Level Analyzer – Problem Overview
"""
A Log Level Analyzer is a program that reads a .log file line by line, identifies the log level in each entry (such as INFO, WARNING, or ERROR),
and counts how many times each level appears. Each log line typically contains a timestamp, a severity level, and a message.
The objective is to parse the structured text correctly, extract the log level reliably, and maintain counters for predefined categories.


The core task involves file handling, parsing structured text, extracting the correct portion of each log line that represents the severity level, and maintaining counters for predefined categories.

A well-designed solution should account for the following scenarios:
1) Case sensitivity – Log levels may appear as info, Info, or INFO.
2) Malformed or empty lines – Some lines may not follow the expected format.
3) Log format variations – The log level may not always be in the same position.
4) False positives – The words “error” or “warning” may appear in the message body but not represent the actual log level.
5) Unexpected log levels – Entries like DEBUG, CRITICAL, or TRACE may exist.
6) Large files – The file could be very large, so reading line-by-line is more memory efficient.
"""

import sys
def log_level_analyzer(filename: str) -> dict[str, int]:
    log: dict[str, int] = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.strip().split()
                if len(words) < 3:
                    continue
                log_word = words[2].upper()
                if log_word in log:
                    log[log_word] += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    return log

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else 'log.txt'
    output = log_level_analyzer(filename)
    with open('output.txt', 'w') as out:
        for word, count in output.items():
            print(f'{word} : {count}')
            out.write(f'{word} : {count}\n')
