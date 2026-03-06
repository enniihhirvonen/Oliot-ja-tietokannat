SELECT
Accounts.city AS city,
AVG(Accounts.balance) AS balance
FROM Accounts
GROUP BY
Accounts.city
ORDER BY
Accounts.city ASC;