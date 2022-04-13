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


def data_input(contact_info):
    with open('input_data.csv', 'r') as f1, open('input_file2.csv', 'r') as f2:
        writer = csv.writer(f1, f2, delimiter='|')
        writer.writerows(contact_info)


def read_file(contact_info):
    with open('input_data.csv', 'r') as f1, open('input_file2.csv', 'r') as f2:
        reader = csv.reader(f1, delimiter='|')
        #reader = csv.reader(f2)

        for row in reader:
            try:
                id, full_name, email, phone_num = row

            except:
                print("Not enough information")

            invalid_data = ''

            try:
                last_name, first_name = full_name.split(', ')
            except:
                invalid_data += 'N'

            email_pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(wsc)'

            try:
                (re.search(email_pattern, email))
            except:
                invalid_data += 'E'

            phone_pattern = '(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
            new_pattern = r'\1.\2.\3'
            try:
                re.sub(phone_pattern, new_pattern)
            except:
                invalid_data += 'P'

        return contact_info


def main():
    """
    The main function
    Args:
        no value
    Returns:
        no value
    """
    contact_info = []
    read_file(contact_info)
    # add_contact_info(contact_info)


if __name__ == '__main__':
    main()
