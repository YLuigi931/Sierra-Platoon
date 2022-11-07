DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
    id                  serial PRIMARY KEY NOT NULL,  
    restaurant_id       integer REFERENCES restaurants(id),
    ordered_items_id    integer NOT NULL
);

DROP TABLE IF EXISTS restaurants;
CREATE TABLE restaurants(
    id                  serial PRIMARY KEY NOT NULL, 
    restaurant_name     VARCHAR(30) NOT NULL,
    restaurant_address  VARCHAR(30) NOT NULL,
    restaurant_city     VARCHAR(30) NOT NULL,
    restaurant_state    VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS menu_items;
CREATE TABLE menu_items(
    id          serial PRIMARY KEY NOT NULL, 
    item_name   VARCHAR(30) NOT NULL,
    item_info   VARCHAR(30) NOT NULL,
    item_price  integer NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id              serial PRIMARY KEY NOT NULL, 
    user_name       VARCHAR(30) NOT NULL,
    user_address    VARCHAR(30) NOT NULL,
    user_city       VARCHAR(30) NOT NULL,
    user_state      VARCHAR(30) NOT NULL
);