import mysql.connector
import logging
import sys
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('data.load')
from data.tables import TABLES

def get_db_connection(db_args):
    connection = None
    try:
        connection = mysql.connector.connect(user=db_args['user'],
        password=db_args['password'],
        host=db_args['host'],
        port=db_args['port'],
        database=db_args['database'])
        logger.debug(f"DB_CONNECTION_ESTABLISHED host={db_args['host']} port={db_args['port']} database={db_args['database']}")
    except Exception as error:
        logger.error(f"Error while connecting to database for job tracker:\n{error}")
        sys.exit(1)
    return connection

def create_tables(connection):
    try:
        cursor = connection.cursor()
        for table_name in TABLES:
            cursor.execute(TABLES[table_name])
        logger.info("TABLE_CREATION_SUCCESS")
    except Exception as e:
        logger.error(f"TABLE_CREATION_FAILURE ex={e}")
        raise e

def get_csv_data(file_path_csv):
    lines = []
    try:
        with open(file_path_csv, 'r') as file:
            for line in file:
                lines.append(tuple(line.split(',')))
    except Exception as error:
        logger.warning("CSV_INGESTION_FAILURE ex={error}")

    logger.info(f"CSV_INGESTION_SUCCESSFUL linesRead={len(lines)}")
    return lines

def insert_many(connection, values):
    if (values is None or len(values) == 0):
        logger.warning(f"NO_VALUES_GIVEN_FOR_INSERTION skipping db insert")
        return
    cursor = connection.cursor()
    insert_stmt = (
        "INSERT INTO ticket (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    try: 
        cursor.executemany(insert_stmt, values)
        connection.commit()
    except Exception as e: 
        logger.warning(f"DB_INSERT_FAILURE ex={e}")
    else:
        logger.info(f"DB_INSERT_SUCCESSFUL recordsInserted={cursor.rowcount}")
    cursor.close()

def load_third_party(connection, file_path_csv):
    values = get_csv_data(file_path_csv)
    insert_many(connection, values)
