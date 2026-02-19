#!/usr/bin/python3
import csv
import requests


def fetch_and_print_posts():
    """Fetch and print post titles from JSONPlaceholder."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title", ""))


def fetch_and_save_posts():
    """Fetch posts and save id, title, body to posts.csv."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        rows = []
        for post in posts:
            rows.append(
                {
                    "id": post.get("id"),
                    "title": post.get("title", ""),
                    "body": post.get("body", ""),
                }
            )

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
