#!/usr/bin/env python3

"""
This script includes multiple functions to read an input file that outputs
both valid and invalid data files
"""

__author__ = 'Lacie Cruise, Kyla Phillips'
__version__ = '1.0'
__copyright__ = 'Coding Competition'
__github__ = 'https://github.com/Ljcruise/Coding_Comp.git'

import csv
import re
import sys

valid_count = 0
invalid_count = 0


def read_file(valid_count, invalid_count):
    with open('input_data.csv', 'r') as f1, open('valid_data.csv', 'w') as f2, open('invalid_data.csv', 'w') as f3:
        input_reader = csv.reader(f1, delimiter='|')
        valid_writer = csv.writer(f2)
        invalid_writer = csv.writer(f3)

        for row in input_reader:

            invalid_data = ''

            try:
                id, full_name, email, phone_num = row
            except:
                invalid_data += 'L'

            try:
                id_num = (int(id))
                id_num >= 0

            except:
                invalid_data += 'I'

            try:
                last_name, first_name = full_name.split(',')
            except:
                invalid_data += 'N'

            try:
                email_pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                re.search(email_pattern, email)
            except:
                invalid_data += 'E'

            try:
                phone_pattern = '(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
                new_pattern = r'\1.\2.\3'
                new_phone_num = re.sub(phone_pattern, new_pattern, phone_num)
                phone_num = new_phone_num
            except:
                invalid_data += 'P'

            print(row)

            if invalid_data > '':
                print(invalid_data)
                f3.write(str(row) + '\n')
                invalid_count += 1
            else:
                f2.write(str(row) + '\n')
                valid_count += 1

        return valid_count, invalid_count


def main():
    """
    The main function
    Args:
        no value
    Returns:
        no value
    """
    try:
        read_file(valid_count, invalid_count)
    except FileNotFoundError as e:
        print('FileNotFoundError:', e)
        sys.exit()
    except OSError as e:
        print('OSError:', e)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()
    finally:
        print()
        print('Number of valid records: ' + str(valid_count))
        print('Number of invalid records: ' + str(invalid_count))


if __name__ == '__main__':
    main()
