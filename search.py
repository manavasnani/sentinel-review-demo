"""User search endpoint - DELIBERATELY VULNERABLE for demo purposes."""

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/search")
def search_users():
    name = request.args.get("name", "")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, email FROM users WHERE name LIKE '%" + name + "%'"
    )
    rows = cursor.fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/user/<user_id>")
def get_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT id, name, email FROM users WHERE id = {user_id}"
    cursor.execute(query)
    row = cursor.fetchone()
    if not row:
        return "Not found", 404
    return jsonify(dict(row))