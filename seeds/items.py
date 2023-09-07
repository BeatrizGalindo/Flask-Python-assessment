from flask_seeder import Seeder

from market.models import Item

items = [Item(id=1, name="IPhone", price=800, barcode="123456789", description="an iphone"),
         Item(id=2, name="IPad", price=700, barcode="123456788", description="an Ipad")]

class ItemsSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    Item.__table__.drop(self.db.engine)
    Item.__table__.create(self.db.engine)
    for item in items:
      print("Adding item: %s" % item)
      self.db.session.add(item)
