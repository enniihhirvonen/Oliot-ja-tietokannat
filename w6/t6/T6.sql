SELECT
f.fruit AS fruit,
f.value AS amount
FROM Fruits f
WHERE f.value > 5000
GROUP BY f.fruit
ORDER BY f.fruit ASC;