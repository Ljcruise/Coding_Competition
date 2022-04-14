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


def read_file():
    global valid_count, invalid_count
    with open('input_data.csv', 'r', newline='') as f1, open('valid_data.csv', 'w', newline='') as f2,\
            open('invalid_data.csv', 'w', newline='') as f3:
        input_reader = csv.reader(f1, delimiter='|')
        valid_writer = csv.writer(f2)
        invalid_writer = csv.writer(f3, delimiter='|')

        for row in input_reader:

            invalid_data = ''

            try:
                id, full_name, email, phone_num = row
            except:
                invalid_data += 'L'
                invalid_writer.writerow([invalid_data, row])
                invalid_count += 1
                continue

            try:
                id_num = int(id)
                id_num >= 0
            except:
                invalid_data += 'I'

            try:
                last_name, first_name = full_name.split(',')
            except:
                invalid_data += 'N'

            email_pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
            m = re.search(email_pattern, email)
            if m == None:
                invalid_data += 'E'

            phone_pattern = '(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
            match = re.search(phone_pattern, phone_num)
            if match == None:
                invalid_data += 'P'
            else:
                new_pattern = r'\1.\2.\3'
                phone_num = re.sub(phone_pattern, new_pattern, phone_num)

            print(row)

            if invalid_data > '':
                print(invalid_data)
                invalid_writer.writerow([invalid_data, row])
                invalid_count += 1
            else:
                valid_writer.writerow([row])
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
        read_file()

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
