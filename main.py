import os
from data.load import *
from cli.cli import *


db_args = get_optional_args()
connection = get_db_connection(db_args)
file_path = os.path.join('data', 'third_party_sales_1.csv')
print("***LOADING DATA***")
create_tables(connection)
load_third_party(connection, file_path)
start_cli(connection)

connection.close()
