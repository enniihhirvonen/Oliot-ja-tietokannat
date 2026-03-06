SELECT
Students.id AS [opiskelija tunnus],
Students.name AS 'nimi',
Students.group_id AS 'ryhma',
Students.ects AS 'ECTS'
FROM Students
WHERE Students.ects = (
    SELECT MAX(s2.ects)
    FROM Students s2
    WHERE s2.group_id = Students.group_id
)
ORDER BY
Students.group_id ASC;