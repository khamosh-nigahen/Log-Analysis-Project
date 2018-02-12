#!/usr/bin/env python3

import psycopg2
import os

# Database Name
DB_NAME = "news"

# Filename
FILENAME = "log_analysis.txt"

# queries
first_query = "select title,views from view_article limit 3"
second_query = "select * from view_author"
third_query = "select * from view_error_log where percent_error > 1"

# to store results
first_query_dict = dict()
first_query_dict['title'] = """\n1. The 3 most popular articles \
of all time are:\n"""

second_query_dict = dict()
second_query_dict['title'] = """\n2. The most popular article \
authors of all time are:\n"""

third_query_dict = dict()
third_query_dict['title'] = """"\n3. Days with more than 1% of \
request that lead to an error:\n"""


def connect_db_get_query_result(query):
    """connects to DB and gets query results"""
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def display_query_result(query_result):
    """prints reports generated from query"""
    print(query_result['title'])
    f = open(FILENAME, 'a')
    f.write(query_result['title'])
    for result in query_result['results']:
        output = ('\t'+str(result[0])+' ---> '+str(result[1])+' views'+'\n')
        f.write(output)
        print(output, end='')
    f.close()


def display_request_error_result(query_result):
    """displays % of requests lead to errors"""
    print(query_result['title'])
    f = open(FILENAME, 'a')
    f.write(query_result['title'])
    for result in query_result['results']:
        output = ('\t'+str(result[0])+' ---> '+str(result[1])+' %'+'\n')
        f.write(output)
        print(output, end='')
    f.close()


# main starts
if __name__ == "__main__":
    print("Fetching the data from the Database...")
    if os.path.isfile(FILENAME):
        os.remove(FILENAME)

    # stores query result
    first_query_dict['results'] = connect_db_get_query_result(first_query)
    second_query_dict['results'] = connect_db_get_query_result(second_query)
    third_query_dict['results'] = connect_db_get_query_result(third_query)

    # print formatted output
    display_query_result(first_query_dict)
    display_query_result(second_query_dict)
    display_request_error_result(third_query_dict)
