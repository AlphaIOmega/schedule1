# Product Viewer

A web application for viewing and analyzing product data from a game. This application displays products, their properties, prices, and crafting recipes.

## Features

- View all discovered products in a grid layout
- Filter products by name
- Sort products by name or price
- View detailed information about each product:
  - Name and ID
  - Price
  - Drug type
  - Properties
  - Appearance colors
  - Crafting path and recipe tree

## Project Structure

```
product_viewer/
│
├── app.py                 # Main Flask application
│
├── data/                  # Data directory
│   ├── Products.json      # Main products data
│   │
│   └── CreatedProducts/   # Individual product files
│       └── afghancake.json
│
├── static/                # Static files
│   └── css/
│       └── style.css      # CSS styling
│
└── templates/             # HTML templates
    ├── base.html          # Base template with common layout
    ├── index.html         # Product list page
    └── product_detail.html # Product detail page
```

## Installation and Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install flask
   ```
3. Place your Products.json file and individual product files in the appropriate directories:
   - Main Products.json file in the `data/` directory
   - Individual product JSON files in the `data/CreatedProducts/` directory

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000/`

## Technologies Used

- Python 3
- Flask (web framework)
- HTML5
- CSS3
- JavaScript (for client-side filtering and sorting)

## Notes

- The application expects the Products.json file to contain information about all products, including their prices and mixing recipes.
- Individual product JSON files (like afghancake.json) should contain detailed information about each product, including its name, properties, and appearance settings.
