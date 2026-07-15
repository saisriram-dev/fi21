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
