class EmployeeUserRecord:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f'Employee User Record: {self.id} {self.username} {self.email}'


class EmployeeNameRecord:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Employee Name Record: {self.id} {self.first_name} {self.last_name}'


class EmployeeSalaryRecord:
    def __init__(self, id, salary_pounds):
        self.id = id
        self.salary_pounds = salary_pounds

    def __str__(self):
        return f'Employee Salary Record: {self.id} £{self.salary_pounds}'


def select_all(connection):
    return connection.run('SELECT * FROM employees;')


def select_by_id(connection, id):
    return connection.run('SELECT * FROM employees WHERE employee_id = :id;', id=id)


def select_by_username(connection, username):
    return connection.run('SELECT * FROM employees WHERE employee_username = :username;', username=username)


def select_by_email(connection, email):
    return connection.run('SELECT * FROM employees WHERE employee_email = :email;', email=email)


def select_by_first_name(connection, first_name):
    query = 'SELECT employee_id, employee_first_name, employee_last_name ' \
            'FROM employee_names WHERE employee_first_name = :first_name;'

    return connection.run(query, first_name=first_name)


def generate_employee_records(rows, table_name):

    def generate_user_record(row):
        id = row[0]
        username = row[1]
        email = row[2]
        return EmployeeUserRecord(id, username, email)

    def generate_name_record(row):
        id = row[0]
        first_name = row[1]
        last_name = row[2]
        return EmployeeNameRecord(id, first_name, last_name)

    def generate_salary_record(row):
        id = row[0]
        salary_pounds = row[1]
        return EmployeeSalaryRecord(id, salary_pounds)

    """ Find the appropriate generator"""
    generators = {
        'employees': generate_user_record,
        'employee_names': generate_name_record,
        'employee_salaries': generate_salary_record,
    }

    """table_name is invalid"""
    if table_name not in generators:
        raise KeyError(
            f'cannot generate employee records because table "{table_name}" is invalid')

    generator = generators[table_name]

    for row in rows:
        yield generator(row)
