from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'book_name': '',
        'author': '',
        'publisher': ''
    },
    
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(book)
    return jsonify(book)

if __name__ == '__main__':
    app.run(debug=True)