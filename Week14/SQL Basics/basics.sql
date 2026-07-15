-- Query 1: Retrieve all science fiction books published after 2015
SELECT *
FROM Books
WHERE Genre = 'Science Fiction'
AND PublishedYear > 2015;

-- Query 2: Find all employees earning more than $100,000
SELECT *
FROM Employees
WHERE salary > 100000;

-- Query 3: Display all employees sorted by salary in descending order (highest to lowest)
SELECT *
FROM Employees
ORDER BY salary DESC;

-- Query 4: Get the top 3 highest-paid employees
SELECT *
FROM Employees
ORDER BY salary DESC
LIMIT 3;

-- Query 5: Calculate the average salary across all employees
SELECT AVG(salary) AS average_salary
FROM Employees;

-- Query 6: Find the maximum salary in the company
SELECT MAX(salary)
FROM Employees;

-- Query 7: Calculate average salary by department
SELECT department,
       AVG(salary) AS average_salary
FROM Employees
GROUP BY department;

-- Query 8: Count the number of employees in each department
SELECT department,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY department;

-- Query 9: Find departments where average salary exceeds $100,000
SELECT department,
       AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 100000;