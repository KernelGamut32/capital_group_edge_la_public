import psycopg2
from orders.models.order import Order
from orders.models.product import Product


class OrderRepository():
    # If you use set environment variables, you could set PGHOST, PGDATABASE,
    # PGUSER, and PGPASSWORD variables in your environment and then you could
    # use the following code to connect to your database.
    # with psycopg2.connect() as db:
    #     with db.cursor() as cursor:
    #         cursor.execute("SELECT * FROM ORDER_DETAIL;")
    #         rows = cursor.fetchall()
    #         for row in rows:
    #             print(row)

    host = "localhost"
    database = "orders"
    user = "postgres"
    password = "password123"

    def insert(self, order: Order):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO ORDER_DETAIL
                        (ORDER_NUMBER, PRODUCT_ID, QUANTITY, TOTAL) VALUES
                        (%(order_number)s, %(product_id)s, %(quantity)s, %(total)s)
                        RETURNING ID
                    """, {
                    'order_number': order.order_number,
                    'product_id': order.product.id,
                    'quantity': order.quantity,
                    'total': round(order.total, 2)
                }
                )
                order.id = cursor.fetchone()[0]
        return order

    def get_by_number(self, order_number):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, ORDER_NUMBER, PRODUCT_ID, QUANTITY, TOTAL FROM ORDER_DETAIL WHERE ORDER_NUMBER=%(order_number)s
                    """, {
                    'order_number': order_number
                }
                )
                row = cursor.fetchone()
                if row:
                    product = Product(id=row[2], product_number='',
                                      description='', unit_cost=0.0)
                    return Order(id=row[0], order_number=row[1], product=product, quantity=row[3], total=row[4])
                else:
                    return None

    def delete(self, id):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM ORDER_DETAIL WHERE ID=%(id)s
                    """, {
                    'id': id
                }
                )
