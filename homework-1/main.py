"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# Создаем соединение с нужной базой данных
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="Timur3370"
)

# Открываем файл csv
with open('C:/Users/USER/PycharmProjects/postgres-homeworks/homework-1/north_data/employees_data.csv', newline='',
          encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # Cчитываем данные из файла
    for row in reader:
        employee_id = row.get('employee_id')
        first_name = row.get('first_name')
        last_name = row.get('last_name')
        title = row.get('title')
        birth_date = row.get('birth_date')
        notes = row.get('notes')
        # Добавляем данные в нужную таблицу
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (employee_id, first_name, last_name,
                                                                                  title, birth_date, notes))
            cur.execute("SELECT * FROM employees")
            # Сохраняем изменения
            conn.commit()

with open('C:/Users/USER/PycharmProjects/postgres-homeworks/homework-1/north_data/customers_data.csv', newline='',
          encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        customer_id = row.get('customer_id')
        company_name = row.get('company_name')
        contact_name = row.get('contact_name')
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (customer_id, company_name, contact_name))
            cur.execute("SELECT * FROM customers")
            conn.commit()

with open('C:/Users/USER/PycharmProjects/postgres-homeworks/homework-1/north_data/orders_data.csv', newline='',
          encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        order_id = row.get('order_id')
        customer_id = row.get('customer_id')
        employee_id = row.get('employee_id')
        order_date = row.get('order_date')
        ship_city = row.get('ship_city')
        with conn.cursor() as cur:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order_id, customer_id, employee_id,
                                                                           order_date, ship_city))
            cur.execute("SELECT * FROM orders")
            conn.commit()
# Закрываем соединение
conn.close()
