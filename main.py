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
    """
    The read file function opens the input, valid and invalid files. It reads the input file then
    goes through each row to validate the id, name, email, and phone number. If the row passes
    all validation, it is written to the valid data file in comma delimited notation. If the row
    failed any or all validation, it is written to the invalid data file in pipe delimited notation.
    Counters are used to keep track of the number of valid and invalid records found.
    Args:
        no value
    Returns:
        valid_count (int): The number of valid records
        invalid_count (int): The number of invalid records
    """
    global valid_count, invalid_count
    with open('input_data.csv', 'r', newline='') as f1, open('valid_data.csv', 'w', newline='') as f2, \
            open('invalid_data.csv', 'w', newline='') as f3:
        input_reader = csv.reader(f1, delimiter='|')   # change the delimiter for the input reader
        valid_writer = csv.writer(f2)   # default delimiter is comma delimited for the valid writer
        invalid_writer = csv.writer(f3, delimiter='|')   # change the delimiter for the invalid writer

        for row in input_reader:

            invalid_data = ''   # set invalid data to a blank string to add to throughout validation

            try:
                id, full_name, email, phone_num = row   # unpack row
            # write to invalid file L followed by the row, add one to invalid count
            except:
                invalid_data += 'L'   # L is invalid record length
                row.insert(0, invalid_data)
                invalid_writer.writerow(row)
                invalid_count += 1
                continue

            # check to see if the id number is a positive integer
            try:
                id_num = int(id)
                id_num >= 0
            except:
                invalid_data += 'I'   # I is invalid ID

            # use the split function to get first and last name
            try:
                last_name, first_name = full_name.split(',')
            except:
                invalid_data += 'N'   # N is invalid name

            # use a regex expression to validate email
            email_pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
            m = re.search(email_pattern, email)
            if m == None:
                invalid_data += 'E'   # E is invalid email

            # use a regex expression to validate phone number format
            phone_pattern = '(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
            match = re.search(phone_pattern, phone_num)
            if match == None:
                invalid_data += 'P'   # P is invalid phone number
            # replace the dashed with periods for valid phone numbers only
            else:
                new_phone_num = phone_num.replace('-', '.')

            # check if the invalid data is more than a blank string
            if invalid_data > '':
                row.insert(0, invalid_data)   # insert invalid data at the beginning of the row list
                invalid_writer.writerow(row)   # write one row at a time to the invalid data file
                invalid_count += 1   # add one to invalid count
            else:
                # write one row at a time to the valid data file
                valid_writer.writerow([id, first_name, last_name, email, new_phone_num])
                valid_count += 1   # add one to valid count

        return valid_count, invalid_count


def main():
    """
    The main function uses try and except to read the files and do the validations.
    It displays errors if it cannot open, read, or write to a file. Then it displays
    the number of valid and invalid records.
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
        print('Number of valid records: ' + str(valid_count))
        print('Number of invalid records: ' + str(invalid_count))


if __name__ == '__main__':
    main()
