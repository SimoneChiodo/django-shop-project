# Progetto Django: Django Shop Project

## 📖 Descrizione
**Django Shop Project** è una **piccola applicazione web** sviluppata in **Django** per la gestione di **clienti, prodotti e ordini**.  
Il progetto combina funzionalità di **backend**, logiche **automatizzate nel database PostgreSQL** e l’uso della **shell Django** per la gestione e visualizzazione dei dati.  

Include un file `guide.md` che guida passo passo l’utente: dalla creazione del progetto e delle app Django, alla definizione dei modelli, fino all’interazione con il database tramite shell.  
L’esercizio è pensato per consolidare competenze pratiche su **Django ORM**, **migrazioni**, e **trigger/funzioni SQL**.


## 🎯 Obiettivo
Creare un sistema completo per la gestione degli ordini che permetta di:
- Registrare e visualizzare **clienti, prodotti e ordini**.  
- Aggiornare automaticamente i **totali spesi dai clienti** tramite trigger nel database.  
- Esercitarsi con l’interazione diretta ai dati tramite la **shell Django**.


## 🌍 Funzionalità principali

### **Gestione clienti**
- **Creazione di clienti tramite shell Django**
  ```python 
  from orders.models import Customer
  c1 = Customer.objects.create(name="Simone", email="simone@example.com")
  ```
- **Visualizzazione di tutti i clienti**
  ```python 
  Customer.objects.all()
  ```
- **Aggiornamento dati e trigger**
  ```python 
  c1.refresh_from_db()
  ```

### **Gestione prodotti**
- **Creazione di prodotti tramite shell Django**
  ```python 
  from orders.models import Product
  p1 = Product.objects.create(name="Tastiera", price=49.90)
  p2 = Product.objects.create(name="Mouse", price=25.00)
  p3 = Product.objects.create(name="Monitor", price=200.00)
  ```
- **Visualizzazione dei prodotti**
  ```python 
  Product.objects.all()
  for p in Product.objects.all():
    print(p.name, p.price)
  ```

### **Gestione ordini**
- **Creazione di ordini tramite shell Django**
  ```python 
  from orders.models import Order
  Order.objects.create(customer=c1, product=p1, quantity=2, total_price=2*p1.price)
  Order.objects.create(customer=c1, product=p2, quantity=1, total_price=p2.price)
  Order.objects.create(customer=c1, product=p3, quantity=1, total_price=p3.price)
  ```
- **Visualizzazione ordini e dettagli leggibili**
  ```python 
  Order.objects.all()
  for o in Order.objects.all():
    print(o.id, o.customer.name, o.product.name, o.quantity, o.total_price)
  ```

### **Trigger e funzioni SQL**
- Funzione PostgreSQL `aggiorna_totale_cliente()` che aggiorna automaticamente il totale speso da un cliente.
- Trigger `trg_update_total` sulla tabella `orders_order` che chiama la funzione dopo ogni inserimento.
- Possibilità di includere script SQL versionati per ricreare trigger e funzioni su nuovi database.

### **Vista aggregata**
- View SQL `vista_clienti_media` che mostra la media della spesa per ordine di ciascun cliente.
- Accessibile sia tramite Django ORM sia tramite query SQL dirette


## 🛠️ Tecnologie utilizzate
- **Python & Django** → backend e gestione logica applicativa.  
- **PostgreSQL** → database relazionale per memorizzazione dati e logica automatica.  
- **PL/pgSQL** → funzioni e trigger per logiche automatiche nel database.  
- **pgAdmin** → gestione visiva di tabelle, trigger e dati.  
- **.env** → gestione sicura di secret key, debug e credenziali DB.
