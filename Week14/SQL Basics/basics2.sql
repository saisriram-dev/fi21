-- Get the 5 oldest employees
SELECT *
FROM employees_table
ORDER BY age DESC   -- sort by age, highest first
LIMIT 5;             -- return only top 5 rows

-- Retrieve all users, sorted by city (A-Z), then by age (highest first) within each city
SELECT *
FROM users
ORDER BY city ASC, age DESC;

-- Insert 3 new rows into the users table
INSERT INTO users (id, username, age, city)
VALUES (1, 'john_doe', 30, 'New York'),
       (2, 'jane_smith', 25, 'Los Angeles'),
       (3, 'alice_jones', 28, 'Chicago');

-- Increment age by 1 for every user in New York
UPDATE users
SET age = age + 1
WHERE city = 'New York';

-- Delete users aged between 20 and 25 (inclusive on both ends)
DELETE FROM users
WHERE age BETWEEN 20 AND 25;

-- LIKE operator: find users whose username starts with 'a'
-- '%' is a wildcard matching zero or more characters
SELECT *
FROM users
WHERE username LIKE 'a%';

-- Wildcard example: find users whose city CONTAINS 'York' anywhere in the string
SELECT *
FROM users
WHERE city LIKE '%York%';

-- Categorize users into age groups using CASE (like if/else in SQL)
-- FIX: changed "fullname" to "username" since that's the actual column in this table
SELECT
    username,
    age,
    CASE
        WHEN age < 18 THEN 'Minor'
        WHEN age BETWEEN 18 AND 64 THEN 'Adult'
        ELSE 'Senior'
    END AS age_group   -- alias for the computed column
FROM users;

-- Column alias: rename "name" to "user_name" in the output
-- Note: your users table doesn't have a "name" column (it has "username") — adjust if needed
SELECT name AS user_name
FROM users;

-- Table alias: "u" is shorthand for "users", useful in joins or long queries
SELECT u.name
FROM users AS u;

-- UPPER(): converts string to uppercase
SELECT UPPER(name)
FROM users;

-- CONCAT(): joins strings together, here combining name and city with a separator
SELECT CONCAT(name, ' - ', city)
FROM users;
