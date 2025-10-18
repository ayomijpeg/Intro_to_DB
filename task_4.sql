-- A script that prints the full description of the table 'books'
-- from the database 'alx_book_store' without using DESCRIBE or EXPLAIN.

SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_DEFAULT
FROM 
    information_schema.columns
WHERE 
    table_schema = 'alx_book_store' AND table_name = 'books';

