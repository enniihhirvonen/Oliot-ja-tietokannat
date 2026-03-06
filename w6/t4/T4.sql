SELECT
Students.group_id AS 'group',
SUM(Students.ects) AS [total ects]
FROM Students
GROUP BY Students.group_id
ORDER BY Students.group_id ASC;