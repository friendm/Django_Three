import os
import sys

sql_lite_database="test_database.db"

BASE_PATH = os.path.abspath(__file__)
for i in range(5):
	BASE_PATH=os.path.dirname(os.path.abspath(__file__))

BASE_PATH=BASE_PATH+"/"+sql_lite_database

print BASE_PATH
