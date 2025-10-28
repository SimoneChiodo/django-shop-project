-- Funzione per aggiornare total_spent
CREATE OR REPLACE FUNCTION aggiorna_totale_cliente()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE orders_customer
  SET total_spent = total_spent + NEW.total_price
  WHERE id = NEW.customer_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger per aggiornare total_spent dopo ogni ordine
CREATE TRIGGER trg_update_total
AFTER INSERT ON orders_order
FOR EACH ROW
EXECUTE FUNCTION aggiorna_totale_cliente();
