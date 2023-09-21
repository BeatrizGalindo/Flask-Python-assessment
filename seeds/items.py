from flask_seeder import Seeder

from market import bcrypt
from market.models import Item, User

items = [Item(id=1, name="IPhone", price=800, barcode="123456789", description="The latest IPhone"),
         Item(id=2, name="IPad", price=700, barcode="987654331", description="The latest Ipad"),
         Item(id=3, name="Book", price=20, barcode="456123789", description="How to understand Flask"),
         Item(id=4, name="Pencil", price=5, barcode="789123456", description="Just a simple pencil"),
         Item(id=5, name="Keyboard", price=50, barcode="321698751", description="Very useful for coding"),
         Item(id=6, name="Trackpad", price=60, barcode="221698751",
              description="Latest track pad very useful for coding")
         ]

users = [User(id=1, username="Beatriz", email_address="beatriz@users.com", password_hash="654321", budget=2000),
         User(id=2, username="Admin", email_address="admin@users.com", password_hash="123456", budget=2000),
         User(id=3, username="Noah", email_address="noah@users.com", password_hash="223456", budget=2000),
         User(id=4, username="Oliver", email_address="oliver@users.com", password_hash="333456", budget=2000),
         User(id=5, username="Arthur", email_address="arthur@users.com", password_hash="444456", budget=2000)]


def password(plain_text_password):
    password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    return password_hash


class ItemsSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
        Item.__table__.drop(self.db.engine)
        Item.__table__.create(self.db.engine)

        for item in items:
            print("Adding item: %s" % item)
            self.db.session.add(item)


class UserSeeder(Seeder):
    def run(self):
        User.__table__.drop(self.db.engine)
        User.__table__.create(self.db.engine)

        for user in users:
            user.password_hash = password(user.password_hash)
            print("Adding item: %s" % user)
            print("Adding item: %s" % user.password_hash)
            self.db.session.add(user)
