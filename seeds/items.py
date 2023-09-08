from flask_seeder import Seeder

from market.models import Item, User

items = [Item(id=1, name="IPhone", price=800, barcode="123456789", description="The latest IPhone"),
         Item(id=2, name="IPad", price=700, barcode="987654331", description="The latest Ipad"),
         Item(id=3, name="Book", price=20, barcode="456123789", description="How to understand Flask"),
         Item(id=4, name="Pencil", price=5, barcode="789123456", description="Just a simple pencil"),
         Item(id=5, name="Keyboard", price=50, barcode="321698751", description="Very useful for coding")
         ]

users = [User(id=1, username="Beatriz", email_address="beatriz@users.com", password_hash = 654321, budget=2000),
         User(id=2, username="Admin", email_address="admin@users.com", password_hash = 123456, budget=2000)]

class ItemsSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    Item.__table__.drop(self.db.engine)
    Item.__table__.create(self.db.engine)

    for item in items:
      print("Adding item: %s" % item)
      self.db.session.add(item)

  # def run(self):
  #   User.__table__.drop(self.db.engine)
  #   User.__table__.create(self.db.engine)
  #
  #   for user in users:
  #     print("Adding item: %s" % user)
  #     self.db.session.add(user)
