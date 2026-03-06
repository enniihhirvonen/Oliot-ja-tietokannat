SELECT
f.fruit AS fruit
FROM Fruits f
WHERE f.fruit LIKE '_a%'
GROUP BY f.fruit
ORDER BY f.fruit ASC;