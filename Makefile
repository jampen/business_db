init-db:
	psql -f sql/create-database.sql
	psql -f sql/create-department-tables.sql
	psql -f sql/create-employee-tables.sql