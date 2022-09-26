import sqlite3
from accounts.models.address import Address
from accounts.database.database import Database


class AddressRepository():
    db_name = 'accounts.db'
    _ = Database()

    def insert(self, address: Address):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('INSERT INTO ADDRESS (ADDRESS, CITY, STATE, ZIP_CODE) VALUES \
                (?, ?, ?, ?)', [address.address, address.city, address.state, address.zip_code])
        address.id = cursor.lastrowid
        return address
        
    def get_by_id(self, id):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('SELECT ID, ADDRESS, CITY, STATE, ZIP_CODE FROM ADDRESS WHERE ID=?;', [id])
        row = cursor.fetchone()
        return Address(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])

    def get_all(self):
        results = []
        with sqlite3.connect(self.db_name) as db:
            cursor = db.execute('SELECT ID, ADDRESS, CITY, STATE, ZIP_CODE FROM ADDRESS;')
        rows = cursor.fetchall()
        for row in rows:
            results.append(Address(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4]))
        return results

    def update(self, id, address: Address):
        if id != address.id:
            return False

        with sqlite3.connect(self.db_name) as db:
            db.execute('UPDATE ADDRESS SET ADDRESS=?, CITY=?, STATE=?, ZIP_CODE=? \
                WHERE ID=?;', [address.address, address.city, address.state, address.zip_code, id])
        return True

    def delete(self, id):
        with sqlite3.connect(self.db_name) as db:
            db.execute('DELETE FROM ADDRESS WHERE ID=?;', [id])
        return True
