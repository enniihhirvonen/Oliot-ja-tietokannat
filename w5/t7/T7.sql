SELECT
name,
vitamin,
value
FROM Fruit
Where name NOT IN (
    SELECT name
    FROM Fruit
    WHERE vitamin = 'Folate (folic acid)'
)
ORDER BY
name DESC,
vitamin ASC;