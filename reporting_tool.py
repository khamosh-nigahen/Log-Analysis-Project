#!/usr/bin/env python3

import psycopg2

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
first_query_dict['title'] = "\n1. The 3 most popular articles of all time are:\n"

second_query_dict = dict()
second_query_dict['title'] = "\n2. The most popular article authors of all time are:\n"

third_query_dict = dict()
third_query_dict['title'] = "\n3. Days with more than 1% of request that lead to an error:\n"


#main starts
if __name__ == "__main__":
    print("Fetching the data from the Database...")

