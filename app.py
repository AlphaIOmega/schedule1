from flask import Flask, render_template, request, jsonify
import json
import os
from collections import defaultdict

app = Flask(__name__)

# Load product data from the provided JSON files in the correct locations
def load_product_data():
    # Load Products.json from data directory
    try:
        with open('data/Products.json', 'r') as f:
            products_data = json.load(f)
        print("Successfully loaded Products.json from data directory")
    except Exception as e:
        print(f"Error loading Products.json: {e}")
        products_data = {
            'DiscoveredProducts': [],
            'MixRecipes': [],
            'ProductPrices': []
        }
    
    # Load individual product files from CreatedProducts directory
    product_details = {}
    
    if 'DiscoveredProducts' in products_data:
        for product_id in products_data['DiscoveredProducts']:
            product_file = f'data/CreatedProducts/{product_id}.json'
            try:
                if os.path.exists(product_file):
                    with open(product_file, 'r') as f:
                        product_details[product_id] = json.load(f)
                    print(f"Successfully loaded {product_file}")
            except Exception as e:
                print(f"Error loading {product_file}: {e}")
    
    return products_data, product_details

# Build a crafting tree for a product
def build_crafting_tree(product_id, products_data):
    # Create a dictionary to map products to their ingredients
    recipe_map = {}
    for recipe in products_data['MixRecipes']:
        output = recipe['Output']
        if output not in recipe_map:
            recipe_map[output] = {
                'product': recipe['Product'],
                'mixer': recipe['Mixer']
            }
    
    # Build the crafting path
    crafting_path = []
    
    def get_recipe_chain(current_id, chain=None):
        if chain is None:
            chain = []
        
        # If we've already processed this product or it's a base product, return the chain
        if current_id in chain or current_id not in recipe_map:
            return chain
        
        # Add the current product to the chain
        chain.append(current_id)
        
        # Get the ingredients
        ingredients = recipe_map.get(current_id)
        if ingredients:
            # Process the primary ingredient
            product_ingredient = ingredients['product']
            get_recipe_chain(product_ingredient, chain)
            
            # Process the mixer ingredient
            mixer_ingredient = ingredients['mixer']
            get_recipe_chain(mixer_ingredient, chain)
        
        return chain
    
    # Get the recipe chain
    recipe_chain = get_recipe_chain(product_id)
    
    # Build the full crafting path with ingredients
    for product in recipe_chain:
        if product in recipe_map:
            crafting_path.append({
                'id': product,
                'ingredients': [recipe_map[product]['product'], recipe_map[product]['mixer']]
            })
    
    # Add the final product if it's not in the path yet
    if product_id not in [item['id'] for item in crafting_path]:
        crafting_path.append({
            'id': product_id,
            'ingredients': []
        })
    
    return crafting_path

@app.route('/')
def index():
    products_data, product_details = load_product_data()
    
    # Create a dictionary to map product IDs to prices
    price_map = {item['String']: item['Int'] for item in products_data.get('ProductPrices', [])}
    
    return render_template('index.html', 
                           products=products_data['DiscoveredProducts'],
                           product_details=product_details,
                           price_map=price_map)

@app.route('/product/<product_id>')
def product_detail(product_id):
    products_data, product_details = load_product_data()
    
    # Get product details
    product = product_details.get(product_id)
    
    # If product not found, return 404
    if not product:
        return f"Product {product_id} not found", 404
    
    # Create a dictionary to map product IDs to prices
    price_map = {item['String']: item['Int'] for item in products_data.get('ProductPrices', [])}
    
    # Get the price for this product
    price = price_map.get(product_id, 0)
    
    # Build the crafting tree
    crafting_tree = build_crafting_tree(product_id, products_data)
    
    return render_template('product_detail.html', 
                           product_id=product_id,
                           product=product,
                           price=price,
                           crafting_tree=crafting_tree,
                           product_details=product_details,
                           price_map=price_map)

@app.route('/api/products')
def get_products():
    products_data, product_details = load_product_data()
    return jsonify(products_data['DiscoveredProducts'])

@app.route('/api/product/<product_id>')
def get_product(product_id):
    _, product_details = load_product_data()
    
    if product_id in product_details:
        return jsonify(product_details[product_id])
    else:
        return jsonify({"error": f"Product {product_id} not found"}), 404

@app.route('/api/crafting-tree/<product_id>')
def get_crafting_tree(product_id):
    products_data, _ = load_product_data()
    
    crafting_tree = build_crafting_tree(product_id, products_data)
    return jsonify(crafting_tree)

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    
    # Check if directories exist
    if not os.path.exists('data'):
        print("Warning: 'data' directory not found! Please make sure it exists.")
    
    if not os.path.exists('data/CreatedProducts'):
        print("Warning: 'data/CreatedProducts' directory not found! Please make sure it exists.")
    
    # Start the Flask app
    app.run(debug=True)