import psycopg2

db_config = {
    'host': 'localhost',
    'database': 'Nortwind_traders',
    'user': 'postgres',
    'password': '0000'
}


def execute(config, query, vars):
    with psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query, vars)
            return dict(zip([column[0] for column in cur.description], cur.fetchone()))


def get_product_by_id(config, id):
    query = "SELECT product_id, product_name, category_name, unit_price FROM products LEFT JOIN categories USING(category_id) WHERE product_id=%s LIMIT 1"
    vars = (id,)
    return execute(config, query, vars)


def get_category_by_id(config, id):
    query = "SELECT category_id, category_name, description, ARRAY_AGG(product_name) FROM categories LEFT JOIN products USING(category_id) WHERE category_id=%s GROUP BY category_id, category_name, description LIMIT 1"
    vars = (id,)
    return execute(config, query, vars)

