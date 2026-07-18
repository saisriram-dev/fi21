-- COUNT(): returns the number of rows
-- COUNT(*) counts all rows, including NULLs in any column
SELECT COUNT(*) AS total_users
FROM users;

-- COUNT(column): counts only non-NULL values in that column
SELECT COUNT(city) AS users_with_city
FROM users;

-- SUM(): adds up all values in a numeric column
SELECT SUM(age) AS total_age
FROM users;

-- AVG(): calculates the average (mean) of a numeric column
SELECT AVG(age) AS average_age
FROM users;

-- MIN(): finds the smallest value in a column
SELECT MIN(age) AS youngest_age
FROM users;

-- MAX(): finds the largest value in a column
SELECT MAX(age) AS oldest_age
FROM users;

-- Combining multiple aggregate functions in one query
SELECT
    COUNT(*) AS total_users,
    AVG(age) AS average_age,
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM users;

-- GROUP BY: aggregate functions are often paired with GROUP BY
-- to calculate results per group instead of the whole table
-- Here: count how many users exist in each city
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city;

-- GROUP BY with AVG: average age per city
SELECT city, AVG(age) AS avg_age_per_city
FROM users
GROUP BY city;

-- HAVING: filters groups AFTER aggregation (WHERE can't do this, since WHERE runs before grouping)
-- Here: only show cities with more than 1 user
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
HAVING COUNT(*) > 1;

-- GROUP BY + ORDER BY: group by city, then sort results by user_count descending
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
ORDER BY user_count DESC;

-- DISTINCT with COUNT: count unique cities (removes duplicates before counting)
SELECT COUNT(DISTINCT city) AS unique_cities
FROM users;

-- WHERE: filters INDIVIDUAL ROWS *before* grouping/aggregation happens
-- You CANNOT use an aggregate function (COUNT, SUM, AVG...) inside WHERE
SELECT city, age
FROM users
WHERE age > 25;   -- filters rows where age > 25, one row at a time

-- HAVING: filters GROUPS *after* aggregation happens
-- You CAN and typically DO use aggregate functions inside HAVING
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
HAVING COUNT(*) > 1;   -- filters entire groups based on their aggregated result

-- WHERE + HAVING together: WHERE filters rows first, THEN grouping happens, THEN HAVING filters groups
SELECT city, AVG(age) AS avg_age
FROM users
WHERE age > 20              -- Step 1: keep only rows where age > 20
GROUP BY city                -- Step 2: group the remaining rows by city
HAVING AVG(age) > 25;        -- Step 3: keep only groups whose average age > 25

-- WRONG — this will throw an error, aggregate functions are not allowed in WHERE
-- SELECT city, COUNT(*)
-- FROM users
-- WHERE COUNT(*) > 1
-- GROUP BY city;

-- CORRECT version of the above
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
HAVING COUNT(*) > 1;

-- Each department and its average_salary, but only for departments that have at least 2 employees, 
-- and only include employees whose salary is at least 65,000 in the calculation.

SELECT department, AVG(salary) AS average_salary
FROM employees
WHERE salary >= 65000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY average_salary DESC;
