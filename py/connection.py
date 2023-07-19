import pg8000.native as postgres
import pg8000.exceptions as pg_exceptions
from os import getenv
import employees as employees


class UsernameNotSetError (Exception):
    def __str__(self):
        return 'error: the PGUSER environment variable is not defined'


"""
  Will create a a connection to db_business,
  if the env var PGUSER is not set, a UsernameNotSetError will be raised 
"""


def create_connection():
    user = getenv('PGUSER')

    if user is None:
        raise UsernameNotSetError()

    password = getenv('PGPASS', 'password')
    return postgres.Connection(user=user, password=password, database='db_business')


"""
  Program execution begins here
"""
if __name__ == '__main__':
    try:
        with create_connection() as connection:
            rows = employees.select_by_first_name(connection, 'Benjamin')

            for employee_record in employees.generate_employee_records(rows, 'employee_names'):
                print(employee_record)

    except pg_exceptions.DatabaseError as database_error:
        arguments = database_error.args[0]
        error_code = arguments['C']
        message = arguments['M']
        print('⛔', message, '[error code: %s]' % (error_code))

    except UsernameNotSetError as username_error:
        print('⛔', username_error)
        print('❗', 'to fix this, please prepend the command with PGUSER=(username)')
        print('❗', 'example: PGUSER=admin make run')

    except KeyError as key_error:
        print('🗝️ ', 'key error:', key_error)
