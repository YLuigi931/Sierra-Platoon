SELECT *
FROM enrollments;

SELECT *
FROM students;

-- 1. Select all rows from the `classes` table.
SELECT *
FROM classes;

-- 2. Select the `name` and `credits` from the 
-- `classes` table where the number of credits 
-- is greater than 3.
SELECT 
    classes.name, classes.credits
FROM 
    classes
WHERE 
    credits > 3;

-- 3. All rows from the `classes` 
-- table where credits is an even number.
SELECT *
FROM 
    classes
WHERE 
    credits % 2 = 0;

-- 4. All of Tianna's enrollments 
-- that she hasn't yet received a grade for.
SELECT * 
FROM 
    enrollments
WHERE 
    student_id = 1 AND grade is NULL;

-- 5. All of Tianna's enrollments that she hasn't 
-- yet received a grade for, selected by her first name, 
-- not her `student.id`
-- Function used: inner JOIN
SELECT 
    students.first_name, students.last_name, students.id, 
    enrollments.student_id, enrollments.grade
FROM 
    enrollments INNER JOIN students
ON 
    students.id = enrollments.student_id
WHERE 
    first_name = 'Tianna' AND grade is NULL;

-- 6. All of Tianna's enrollments that she 
-- hasn't yet received a grade for, selected by 
-- her first name, not her `student.id`, with 
-- the class name included in the result set.

-- Function used: multiple inner JOIN
SELECT 
    students.first_name, students.last_name, students.id, 
    enrollments.student_id, enrollments.grade,
    classes.id, classes.name as Class_name
FROM
    students
    INNER JOIN enrollments ON students.id = enrollments.student_id
    INNER JOIN classes ON classes.id = enrollments.class_id
WHERE 
    first_name = 'Tianna' AND grade is NULL;

-- 7. All students born before 1986 who have 
-- a 't' in their first or last name.
-- Function used: extract, substring 
SELECT 
    students.first_name, students.last_name, extract(year from students.birthdate) as Birth_year
FROM 
    students
WHERE
    extract(year from students.birthdate) < 1986 AND
    LOWER(students.first_name) ~~ substring(LOWER(students.first_name) SIMILAR '%t%' escape '#') OR
    LOWER(students.last_name) ~~ substring(LOWER(students.last_name) SIMILAR '%t%' escape '#');

-- 8. The average age of all the students.
-- Functions used: extract, avg and age functions
SELECT extract(
    years from avg(
        age(birthdate))) as Average_age
FROM students;

-- 9. Addresses that have a space in 
-- their city name.
-- Function used: substring
SELECT *
FROM 
    addresses
WHERE
    addresses.city ~~ substring(addresses.city SIMILAR '% %' escape '#');

-- 10. Students & their addresses 
-- that live in a city with more than one 
-- word in the city name.
-- Functions used: Inner join and substring
SELECT 
    students.first_name, students.last_name,
    students.address_id, addresses.id, 
    addresses.line_1, addresses.city, addresses.state
FROM
    students
    INNER JOIN addresses ON students.address_id = addresses.id
WHERE
    addresses.city ~~ substring(addresses.city SIMILAR '% %' escape '#');

-- 11. The average number of credits 
-- for classes offered at the school.
-- Functions used: avg and round

SELECT 
    round(avg(classes.credits), 2) as Average_credit
FROM 
    classes;

-- 12. The first and last name of all students 
-- who have received an 'A'.
-- Function used: INNER JOIN
SELECT 
    students.first_name, students.last_name, enrollments.grade
FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
WHERE
    enrollments.grade = 'A';

-- 13. Each student's first name and the total 
-- credits they've enrolled in.
-- Function used: INNER JOIN and sum
SELECT 
    students.id, students.first_name, sum(classes.credits)
FROM 
    students
    INNER JOIN enrollments on enrollments.student_id = students.id
    INNER JOIN classes on classes.id = enrollments.class_id
GROUP BY   
    students.id, students.first_name;

-- 14. The total number of credits each student 
-- has received a grade for.
-- Function used: same as top
SELECT 
    students.id, students.first_name, sum(classes.credits)
FROM 
    students
    INNER JOIN enrollments on enrollments.student_id = students.id
    INNER JOIN classes on classes.id = enrollments.class_id
WHERE
    enrollments.grade is NOT NULL
GROUP BY   
    students.id, students.first_name;

-- 15. All enrollments, including the class name.
-- Function used: INNER JOIN
SELECT *
FROM enrollments
    INNER JOIN classes on enrollments.class_id = classes.id;

-- 16. Students born between 1982-1985 (inclusive).
-- Function used: EXTRACT 
SELECT 
    students.first_name, students.last_name, EXTRACT(YEAR FROM students.birthdate)
FROM 
    students
WHERE
    extract(year from students.birthdate) >= 1982 AND
    extract(year from students.birthdate) <= 1985;

-- 17. Insert a new enrollment recording that 
-- Andre Rohan took PHYS 218 and got an A.
-- Function used:

INSERT INTO enrollments (id, student_id, class_id, grade) 
VALUES (DEFAULT, 5, 4, 'A');

-- DELETE FROM enrollments
-- WHERE id = 17;

-- SELECT *
-- FROM enrollments;
