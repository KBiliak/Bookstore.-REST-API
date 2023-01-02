from flask import Flask, request


app = Flask(__name__)

books = [
    {"author": "David Thomas", "id": 5, "name": "The pragmatic programmer"},
    {"author": "Ray Dalio", "id": 20, "name": "Principles"},
    {"author": "marty Cagan", "id": 30, "name": "Inspired"}
]


@app.get("/book/<int:id>")
def get_book(id):
    print("Endpoint was called: got book", id)

    for b in books:
        if id == b["id"]:
            return b
    return {}

@app.get("/books")
def get_books():
    print("Endpoint was called: hello")
    return books

@app.post("/book")
def create_book():
    body = request.get_json()
    new_book = {
        "author": body["author"],
        "name": body["name"]
    }
    id = 0
    for book in books:
        if book["id"] > id:
            id = book["id"]
    id = id + 1
    new_book["id"] = id
    books.append(new_book)

    return new_book

