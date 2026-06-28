-- Write your query below
SELECT c1.name
FROM customers c1 LEFT JOIN orders o1 on c1.id = o1.customer_id
WHERE o1.id IS NULL