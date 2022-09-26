import sqlite3
from accounts.models.customer import Customer
from accounts.repositories.address import AddressRepository
from accounts.database.database import Database


class CustomerRepository():
    db_name = 'accounts.db'
    address_repository = AddressRepository()
    _ = Database()

    def insert(self, customer: Customer):
        address = self.address_repository.insert(customer.address)
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('INSERT INTO CUSTOMER (FIRST_NAME, LAST_NAME, ADDRESS_ID, EMAIL_ADDRESS) VALUES \
                (?, ?, ?, ?)', [customer.first_name, customer.last_name, address.id, customer.email_address])
        customer.id = cursor.lastrowid
        return customer

    def get_by_id(self, id):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('SELECT ID, FIRST_NAME, LAST_NAME, ADDRESS_ID, EMAIL_ADDRESS FROM CUSTOMER WHERE ID=?;', [id])
        row = cursor.fetchone()
        address = self.address_repository.get_by_id(row[3])
        return Customer(id=row[0], first_name=row[1], last_name=row[2], address=address, email_address=row[4])

    def get_all(self):
        results = []
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('SELECT ID, FIRST_NAME, LAST_NAME, ADDRESS_ID, EMAIL_ADDRESS FROM CUSTOMER;')
        rows = cursor.fetchall()
        for row in rows:
            address = self.address_repository.get_by_id(row[3])
            results.append(Customer(id=row[0], first_name=row[1], last_name=row[2], address=address, email_address=row[4]))
        return results

    def update(self, id, customer: Customer):
        if id != customer.id:
            return False
        if not self.address_repository.update(customer.address.id, customer.address):
            return False
        with sqlite3.connect(self.db_name) as db:
            db.execute('UPDATE CUSTOMER SET FIRST_NAME=?, LAST_NAME=?, ADDRESS_ID=?, EMAIL_ADDRESS=? \
                WHERE ID=?;', [customer.first_name, customer.last_name, customer.address.id, customer.email_address, id])
        return True

    def delete(self, id):
        customer = self.get_by_id(id)
        if not self.address_repository.delete(customer.address.id):
            return False
        with sqlite3.connect(self.db_name) as db:
            db.execute('DELETE FROM CUSTOMER WHERE ID=?;', [id])
        return True
