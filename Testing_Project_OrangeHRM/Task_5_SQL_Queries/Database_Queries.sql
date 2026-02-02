1. Query to verify if the 'Admin' user exists in the system
SELECT * FROM users WHERE username = 'Admin';

 2. Query to fetch all employees from the PIM module
SELECT employee_name, job_title FROM employees;

 3. Query to check login logs for a specific date
SELECT * FROM login_logs WHERE login_date = '2024-05-20';