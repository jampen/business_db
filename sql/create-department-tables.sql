\c db_business

DROP TABLE IF EXISTS departments;

-- Creating department tables
\echo 'Creating departments table'
CREATE TABLE departments (
  department_id                    SERIAL PRIMARY KEY,
  department_yearly_budget_pounds  INT
);