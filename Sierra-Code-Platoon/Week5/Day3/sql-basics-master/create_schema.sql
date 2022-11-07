
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  birthdate    date NOT NULL,
  address_id   integer
);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
  id SERIAL PRIMARY KEY,
  line_1 VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(255),
  zipcode VARCHAR(255)
);

DROP TABLE IF EXISTS classes;
CREATE TABLE classes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  credits integer NOT NULL
);

DROP TABLE IF EXISTS enrollments;
CREATE TABLE enrollments (
  id SERIAL PRIMARY KEY,
  student_id integer,
  class_id integer,
  grade VARCHAR(255)
);

