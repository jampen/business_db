\c db_business

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS employee_names;
DROP TABLE IF EXISTS employee_departments;
DROP TABLE IF EXISTS employee_salaries;

\echo 'Creating employees table'
CREATE TABLE employees (
  employee_id        SERIAL PRIMARY KEY,
  employee_username  TEXT,
  employee_email     TEXT
);

\echo 'Creating employee names table'
CREATE TABLE employee_names (
  employee_id          INT PRIMARY KEY,
  employee_first_name  TEXT,
  employee_last_name   TEXT
);

\echo 'Creating employee departments table'
CREATE TABLE employee_departments (
  employee_id         INT PRIMARY KEY,
  department_id       INT REFERENCES departments (department_id)
);

\echo 'Creating employee salaries table'
CREATE TABLE employee_salaries (
  employee_id             INT PRIMARY KEY,
  employee_salary_pounds  INT
);