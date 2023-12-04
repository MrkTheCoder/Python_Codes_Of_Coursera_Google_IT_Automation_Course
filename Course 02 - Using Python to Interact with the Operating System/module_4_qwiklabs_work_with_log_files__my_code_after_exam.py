#!/usr/bin/env python3
import sys


def is_line_validated(line, search_words):
    return all(word in line.lower() for word in search_words)


def extract_lines_from_log_file(fullpath_logfile, search_words):
    matched_lines = []

    with open(fullpath_logfile) as log_file:
        for line in log_file:
            validated = is_line_validated(line, search_words)
            if not validated:
                continue
            matched_lines.append(line)

    return matched_lines


def write_log(fullpath_errs, lines):
    with open(fullpath_errs, 'w') as err_file:
        err_file.writelines(lines)


if __name__ == '__main__':
    print()

    IDX_LOG_FILE = 1
    IDX_ERR_FILE = 2
    if len(sys.argv) != 3:
        print(f"Syntax:\n{sys.argv[0]} log_file export_file")
        exit(1)

    print('Please insert word(s) and separate them with ",":')
    words = input()
    word_list = [w.lower().strip() for w in words.split(',')]

    lines = extract_lines_from_log_file(sys.argv[IDX_LOG_FILE], word_list)

    write_log(sys.argv[IDX_ERR_FILE], lines)

    print(f"{len(lines)} line(s) matched the criteria!")
