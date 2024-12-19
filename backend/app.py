from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle CORS
from models import db, Product

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Routes
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('message', '').lower()

    if not query:
        return jsonify({'error': 'Message is required'}), 400

    # Search logic
    products = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    if not products:
        return jsonify({'reply': f'No products found for "{query}"'}), 404

    product_list = [{'id': p.id, 'name': p.name, 'price': p.price} for p in products]
    return jsonify({'reply': 'Here are the matching products:', 'products': product_list})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
