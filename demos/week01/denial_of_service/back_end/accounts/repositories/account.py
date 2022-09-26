import sqlite3
from accounts.models.account import Account
from accounts.repositories.customer import CustomerRepository
from accounts.database.database import Database


class AccountRepository():
    db_name = 'accounts.db'
    customer_repository = CustomerRepository()
    _ = Database()

    def insert(self, account: Account):
        customer = self.customer_repository.insert(account.customer)
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('INSERT INTO ACCOUNT (ACCOUNT_NUMBER, CUSTOMER_ID, CURRENT_BALANCE) VALUES \
                (?, ?, ?)', [account.account_number, customer.id, account.current_balance])
        account.id = cursor.lastrowid
        return account

    def get_by_id(self, id):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('SELECT ID, ACCOUNT_NUMBER, CUSTOMER_ID, CURRENT_BALANCE FROM ACCOUNT WHERE ID=?;', [id])
        row = cursor.fetchone()
        customer = self.customer_repository.get_by_id(row[2])
        return Account(id=row[0], account_number=row[1], customer=customer, current_balance=round(row[3], 2))

    def get_all(self):
        results = []
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('SELECT ID, ACCOUNT_NUMBER, CUSTOMER_ID, CURRENT_BALANCE FROM ACCOUNT;')
        rows = cursor.fetchall()
        for row in rows:
            customer = self.customer_repository.get_by_id(row[2])
            results.append(Account(id=row[0], account_number=row[1], customer=customer, current_balance=round(row[3], 2)))
        return results

    def update(self, id, account: Account):
        if str(id) != str(account.id):
            return False
        if not self.customer_repository.update(account.customer.id, account.customer):
            return False
        with sqlite3.connect(self.db_name) as db:
            db.execute('UPDATE ACCOUNT SET ACCOUNT_NUMBER=?, CUSTOMER_ID=?, CURRENT_BALANCE=? \
                WHERE ID=?;', [account.account_number, account.customer.id, account.current_balance, id])
        return True

    def delete(self, id):
        account = self.get_by_id(id)
        if not self.customer_repository.delete(account.customer.id):
            return False
        with sqlite3.connect(self.db_name) as db:
            db.execute('DELETE FROM ACCOUNT WHERE ID=?;', [id])
        return True
