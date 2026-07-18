-- Query 1: INNER JOIN
-- Goal: Return only employees that have a matching department.
-- Employees with no department (NULL department_id) are excluded,
-- and departments with no employees are excluded too.
SELECT
    e.name,
    d.department_name
FROM employees AS e
JOIN departments AS d
    ON e.department_id = d.department_id;   -- inner join condition


-- Query 2: LEFT JOIN
-- Goal: Return ALL employees, whether or not they have a matching
-- department. If no match is found, d.department_name will be NULL.
SELECT
    e.name,
    d.department_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.department_id = d.department_id;   -- left join keeps all rows from employees


-- Query 3: FULL OUTER JOIN
-- Goal: Return ALL employees AND all departments, matched where
-- possible. Unmatched employees show NULL department_name;
-- unmatched departments show NULL employee name.
-- Note: MySQL does not support FULL OUTER JOIN natively
-- (works in PostgreSQL, SQL Server, Oracle).
SELECT
    e.name,
    d.department_name
FROM employees e
FULL OUTER JOIN departments d
    ON e.department_id = d.id;   -- join condition uses d.id here


-- Query 4: LEFT JOIN with filter INSIDE the ON clause
-- Goal: Return ALL employees. The department info (department_name)
-- is only attached when the department is 'Engineering' — for every
-- other employee, department_name will be NULL, but the employee row
-- is still kept.
-- This is different from putting the filter in WHERE (see Query 5).
SELECT
    e.name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.id
    AND d.department_name = 'Engineering';   -- filter applied before the join, not after


-- Query 5: LEFT JOIN with filter in WHERE clause
-- Goal: Return ONLY employees who belong to the 'Engineering'
-- department. Because the filter is in WHERE (applied after the
-- join), it eliminates all rows where department_name is NULL,
-- which effectively turns this into an INNER JOIN behavior.
SELECT
    e.name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.id
WHERE d.department_name = 'Engineering';   -- filters AFTER the join, removes unmatched rows


-- Query 6: Aggregation with LEFT JOIN, GROUP BY, and HAVING
-- Goal: For each department, calculate the number of employees and
-- their average salary — including departments with ZERO employees
-- (thanks to the LEFT JOIN + COUNT/AVG which ignore NULLs).
-- Only keep departments where:
--   - average salary is 70000 or more, OR
--   - the department has no employees at all (count = 0)
-- Results are sorted by average salary, highest first.
SELECT
    d.department_name,
    COUNT(e.id) AS employee_count,     -- counts non-NULL e.id, so empty depts show 0
    AVG(e.salary) AS average_salary    -- AVG ignores NULLs; will be NULL for empty depts
FROM departments AS d
LEFT JOIN employees AS e
    ON e.department_id = d.id
GROUP BY d.department_name
HAVING AVG(e.salary) >= 70000
    OR COUNT(e.id) = 0                 -- keeps empty departments even though AVG is NULL
ORDER BY average_salary DESC;
