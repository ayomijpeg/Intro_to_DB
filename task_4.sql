-- This script prints the full description of the 'books' table.
-- It retrieves column information from the INFORMATION_SCHEMA.
-- The database name is passed as an argument to the mysql command.
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'books';
