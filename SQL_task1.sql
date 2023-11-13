SELECT c.login,
       COUNT(o.id) AS orders_in_delivery
FROM "Couriers" c
INNER JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;