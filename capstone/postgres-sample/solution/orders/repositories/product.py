import psycopg2
from orders.models.product import Product


class ProductRepository():
    # If you use set environment variables, you could set PGHOST, PGDATABASE,
    # PGUSER, and PGPASSWORD variables in your environment and then you could
    # use the following code to connect to your database.
    # with psycopg2.connect() as db:
    #     with db.cursor() as cursor:
    #         cursor.execute("SELECT * FROM PRODUCT;")
    #         rows = cursor.fetchall()
    #         for row in rows:
    #             print(row)

    host = "localhost"
    database = "orders"
    user = "postgres"
    password = "password123"

    def get_by_id(self, id):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, PRODUCT_NUMBER, DESCRIPTION, UNIT_COST FROM PRODUCT WHERE ID=%(id)s
                    """, {
                    'id': id
                }
                )
                row = cursor.fetchone()
                return Product(id=row[0], product_number=row[1], description=row[2], unit_cost=row[3])

    def get_by_number(self, product_number):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, PRODUCT_NUMBER, DESCRIPTION, UNIT_COST FROM PRODUCT WHERE PRODUCT_NUMBER=%(product_number)s
                    """, {
                    'product_number': product_number
                }
                )
                row = cursor.fetchone()
                if row:
                    return Product(id=row[0], product_number=row[1], description=row[2], unit_cost=row[3])
                else:
                    return None

    def get_all(self):
        results = []
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, PRODUCT_NUMBER, DESCRIPTION, UNIT_COST FROM PRODUCT
                    """)
                rows = cursor.fetchall()
                for row in rows:
                    results.append(
                        Product(id=row[0], product_number=row[1], description=row[2], unit_cost=row[3]))
        return results

    def insert(self, product: Product):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO PRODUCT (PRODUCT_NUMBER, DESCRIPTION, UNIT_COST) VALUES (%(product_number)s, %(description)s, %(unit_cost)s)
                    RETURNING ID
                    """, {
                    'product_number': product.product_number,
                    'description': product.description,
                    'unit_cost': product.unit_cost
                }
                )
                product.id = cursor.fetchone()[0]
                return product

    def update(self, product: Product):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    UPDATE PRODUCT SET PRODUCT_NUMBER=%(product_number)s, DESCRIPTION=%(description)s, UNIT_COST=%(unit_cost)s WHERE ID=%(id)s
                    """, {
                    'id': product.id,
                    'product_number': product.product_number,
                    'description': product.description,
                    'unit_cost': product.unit_cost
                }
                )
        return self.get_by_id(product.id)

    def delete(self, id):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM PRODUCT WHERE ID=%(id)s
                    """, {
                    'id': id
                }
                )
