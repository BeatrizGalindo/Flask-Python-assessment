# Create de Model for the database
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())

    # Create a String
    def __repr__(self):
        return f'Item {self.name}'