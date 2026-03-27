#!/usr/bin/python3
"""Flask app that displays product data from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_JSON = BASE_DIR / "products.json"
PRODUCTS_CSV = BASE_DIR / "products.csv"
PRODUCTS_DB = BASE_DIR / "products.db"


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


def load_products_from_sql(product_id=None):
    """Read product data from the SQLite database."""
    query = "SELECT id, name, category, price FROM Products"
    parameters = ()

    if product_id is not None:
        query += " WHERE id = ?"
        parameters = (product_id,)

    with sqlite3.connect(PRODUCTS_DB) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query, parameters).fetchall()

    return [
        {
            "id": int(row["id"]),
            "name": row["name"],
            "category": row["category"],
            "price": float(row["price"]),
        }
        for row in rows
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

    if product_id is not None:
        try:
            requested_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )
    else:
        requested_id = None

    try:
        if source == "json":
            products_data = load_products_from_json()
            if requested_id is not None:
                products_data = [
                    product
                    for product in products_data
                    if product["id"] == requested_id
                ]
        elif source == "csv":
            products_data = load_products_from_csv()
            if requested_id is not None:
                products_data = [
                    product
                    for product in products_data
                    if product["id"] == requested_id
                ]
        elif source == "sql":
            products_data = load_products_from_sql(requested_id)
        else:
            return render_template(
                "product_display.html",
                error="Wrong source",
                products=[],
            )
    except sqlite3.Error:
        return render_template(
            "product_display.html",
            error="Database error",
            products=[],
        )

    if requested_id is not None and not products_data:
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
