from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # permet d'accéder aux colonnes par nom
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()
    # Convertir en liste de dicts
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Sélection de la source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        try:
            data = read_sql()
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f"Database error: {e}")
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrage par id si fourni
    if product_id is not None:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)