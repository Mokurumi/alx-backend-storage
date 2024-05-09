-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- Quantity in the table items can be negative.

CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - 1 WHERE id = NEW.item_id;
