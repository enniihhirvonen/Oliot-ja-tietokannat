SELECT
Accounts.city as city,
COUNT(Accounts.city) as city_count
FROM Accounts
GROUP BY Accounts.city
HAVING COUNT(*) >= 5
ORDER BY Accounts.city ASC;