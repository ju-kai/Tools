# coding:utf-8

import os
import csv


def csv_to_dict(csv_file):
    try:
        with open(csv_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print row['name'], row['age'], row['address']
    except IOError as(error, strerror):
        print "I/O error({0}):{1}" . format(error, strerror)
    return

currentPath = os.getcwd()
csv_file = currentPath + '/csv/Names.csv'
csv_to_dict(csv_file)


def dict_to_csv(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'w+') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (error, strerror):
        print "I/O error({0}):{1}".format(error, strerror)
    return

csv_columns = ['name', 'age', 'address']
dict_data = [
    {'name': 'lisa', 'age': 15, 'address': 'xian'},
    {'name': 'rose', 'age': 18, 'address': 'beijing'},
    {'name': 'tom', 'age': 22, 'address': 'shanghai'},
    {'name': 'xiaohua', 'age': 33, 'address': 'hangzhou'},
]

currentPath = os.getcwd()
csv_file = currentPath + "/csv/Names.csv"
dict_to_csv(csv_file, csv_columns, dict_data)