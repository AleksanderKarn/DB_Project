import psycopg2
import json

with psycopg2.connect(
        host='localhost',
        database='Nortwind_traders',
        user='postgres',
        password='0000'
) as conn:
    with conn.cursor() as cur:
        with open("suppliers.json", newline='') as f:
            data = json.load(f)

            for i in data:
                cur.execute(
                    "INSERT INTO suppliers (company_name, contact, address, phone, fax, homepage) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                    (i['company_name'], i['contact'], i['address'], i['phone'], i['fax'], i['homepage']))
                suppler_id = cur.fetchone()[0]
                cur.execute(
                    "UPDATE products SET supplier_id = %s WHERE product_name = ANY(%s)",
                    (suppler_id, i['products']))