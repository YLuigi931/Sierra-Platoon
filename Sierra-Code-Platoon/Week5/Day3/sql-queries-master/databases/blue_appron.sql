DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id              serial PRIMARY KEY,
    plan_id         integer NOT NULL,
    user_name       varchar(30) NOT NULL,
    user_address    varchar(55) NOT NULL,
    user_city       varchar(55) NOT NULL,
    user_state      varchar(55) NOT NULL,
    promotion_id    integer NOT NULL
);
DROP TABLE IF EXISTS service_plans;
CREATE TABLE service_plans(
    id               serial PRIMARY KEY,
    serving_size     integer NOT NULL,
    meals_per_week   integer NOT NULL,
    price_USD        DECIMAL(3,2) NOT NULL
);
DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes(
    id              serial PRIMARY KEY,
    name_of_recipe  varchar(30) NOT NULL,
    cook_time_min   DECIMAL(3,2) NOT NULL,
    ingredients     varchar(255) NOT NULL
);
DROP TABLE IF EXISTS  promotions;
CREATE TABLE promotions(
    id          serial PRIMARY KEY,
    promo_name  varchar(25) NOT NULL,
    deduction   integer NOT NULL
);
DROP TABLE IF EXISTS deliveries;
CREATE TABLE deliveries(
    id          serial PRIMARY KEY,
    user_id     integer NOT NULL,
    recipe_id   integer NOT NULL
);