#!/usr/bin/env python3
import os
import re
import sys

TOTAL_ARGS = 4
ARGS_IDX_LOG_FILE = 1
ARGS_IDX_ERR_FILE = 2
ARGS_IDX_SEARCH_WORD = 3
ARGS_IDX_PATTERN = 4


def verify_file(fullpath):
    if not (os.path.exists(fullpath) and os.path.isfile(fullpath)):
        print(f"File not exists: '{fullpath}'")
        exit(2)


def verify_path(path):
    abs_path = os.path.abspath(path)
    only_path = os.path.dirname(abs_path)
    if not os.path.isdir(only_path):
        print(f"Path to save this file is not exists: {path}")
        exit(3)


def is_line_validated(line, search_word, pattern):
    validated = False
    new_line = ''

    if len(search_word) != 0 and search_word not in line:
        return validated, new_line

    result = re.search(pattern, line)
    if result:
        validated = True
        if len(result.groups()):
            new_line = f"{' '.join(result.groups())}"
        else:
            new_line = f"{result[0]}"

    return validated, new_line


def extract_lines_from_log(fullpath_logfile, search_word, pattern):
    verify_file(fullpath_logfile)

    matched_lines = []

    with open(fullpath_logfile) as log_file:
        for line in log_file:
            validated, new_line = is_line_validated(line, search_word, pattern)
            if not validated:
                continue
            matched_lines.append(new_line)

    return matched_lines


def write_new_log(fullpath_errs, matched_words):
    verify_path(fullpath_errs)
    with open(fullpath_errs, 'w') as new_log:
        new_log.writelines(matched_words)


def verify_args():
    # index 0 is always the name of script so we did '- 1' to exclude it!
    if len(sys.argv) - 1 != TOTAL_ARGS:
        print("You must insert 4 arguments!")
        print('Syntax:')
        print(
            f'{sys.argv[0]} log_fullpath err_fullpath [specific_word|""] "pattern"')
        exit(1)


def main():
    print()

    verify_args()

    log_file = sys.argv[ARGS_IDX_LOG_FILE]
    output_file = sys.argv[ARGS_IDX_ERR_FILE]
    search_word = sys.argv[ARGS_IDX_SEARCH_WORD]
    pattern = r'' + sys.argv[ARGS_IDX_PATTERN]

    verify_file(log_file)
    verify_path(output_file)

    print('Start searching...')

    matched_lines = extract_lines_from_log(log_file, search_word, pattern)

    write_new_log(output_file, matched_lines)

    print(f"{len(matched_lines)} line(s) matched the criteria!")


if __name__ == '__main__':
    main()
