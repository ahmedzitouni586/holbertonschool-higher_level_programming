-- Lists all records of second_table
-- Display both score and name (in that order) where score >= 10
-- Ordered by top score first

SELECT
	score,
	name
FROM
	second_table
WHERE
    score >= 10
ORDER BY
	score DESC;
