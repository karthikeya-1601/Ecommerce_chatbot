from models import db, Product
from app import app

# Mock data
products = [
    {
        'name': f'Product {i}',
        'description': f'Description for Product {i}',
        'price': round(10 + i * 1.5, 2)
    }
    for i in range(1, 101)
]

# Populate database
with app.app_context():
    db.create_all()  # Create tables if they don't exist
    for p in products:
        product = Product(name=p['name'], description=p['description'], price=p['price'])
        db.session.add(product)
    db.session.commit()
    print("Database populated with 100 products.")
