-- SCRIPT THAT LISTS ALL RECORDS OF THE TABLE ONLY IF NAME HAS A VALUE
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;