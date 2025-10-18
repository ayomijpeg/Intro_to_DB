-- This script creates the necessary tables for the alx_book_store database.
-- It assumes the database 'alx_book_store' already exists.

-- Select the database to use for the subsequent commands.
USE alx_book_store;

-- Create the Authors table to store author information.
-- author_id is the primary key to uniquely identify each author.
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Create the Books table to store book information.
-- book_id is the primary key.
-- author_id is a foreign key that links to the Authors table.
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Create the Customers table to store customer information.
-- customer_id is the primary key.
-- The email column must contain unique values.
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE NOT NULL,
    address TEXT
);

-- Create the Orders table to store order information.
-- order_id is the primary key.
-- customer_id is a foreign key that links to the Customers table.
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create the Order_Details table to link Orders and Books.
-- This table represents a many-to-many relationship.
-- order_detail_id is the primary key.
-- order_id links to the Orders table.
-- book_id links to the Books table.
CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

