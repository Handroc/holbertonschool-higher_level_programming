#!/usr/bin/python3
"""Flask app that displays product data from JSON or CSV files."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_JSON = BASE_DIR / "products.json"
PRODUCTS_CSV = BASE_DIR / "products.csv"


def load_products_from_json():
    """Read product data from the JSON file."""
    with PRODUCTS_JSON.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        {
            "id": int(product["id"]),
            "name": product["name"],
            "category": product["category"],
            "price": float(product["price"]),
        }
        for product in data
    ]


def load_products_from_csv():
    """Read product data from the CSV file."""
    with PRODUCTS_CSV.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return [
            {
                "id": int(product["id"]),
                "name": product["name"],
                "category": product["category"],
                "price": float(product["price"]),
            }
            for product in reader
        ]


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render the contact page."""
    return render_template("contact.html")


@app.route("/products")
def products():
    """Render product data from the selected source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        products_data = load_products_from_json()
    elif source == "csv":
        products_data = load_products_from_csv()
    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[],
        )

    if product_id is not None:
        try:
            requested_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )

        products_data = [
            product for product in products_data if product["id"] == requested_id
        ]
        if not products_data:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )

    return render_template(
        "product_display.html",
        error=None,
        products=products_data,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
