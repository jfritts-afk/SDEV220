import os  # Import operating system for screen clearing
import time  # Import time for delays

# Clear the screen based on the operating system
os.system('cls' if os.name == 'nt' else 'clear')

# Display a welcome message
print("Welcome to the Bookstore Database!")

# Introduce a 5-second delay
time.sleep(5)

# Clear the screen again based on the operating system
os.system('cls' if os.name == 'nt' else 'clear')

import signal
import socket
import logging
import argparse
import threading
import importlib
import subprocess
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError  # Import SQLAlchemy exceptions
from flask import Flask, request, jsonify, render_template, redirect, url_for

# Configure logging to a file
logging.basicConfig(filename='app.log', level=logging.ERROR)

# Function to check and install packages
def check_and_install(package):
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"Installing {package}...")
        try:
            process = subprocess.Popen(["pip", "install", package], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            for line in process.stdout:
                print(line.strip())
            process.wait()
            if process.returncode == 0:
                print(f"{package} installed successfully.")
            else:
                print(f"Failed to install {package}. Please install it manually.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}. Please install it manually.")

# Check and install required packages
def install_required_packages():
    packages = ["Flask", "SQLAlchemy", "Flask-SQLAlchemy"]
    for package in packages:
        print(f"Checking for {package}")
        time.sleep(2)
        check_and_install(package)
        os.system('cls' if os.name == 'nt' else 'clear')

# Parse command-line arguments for host and port
def parse_arguments():
    parser = argparse.ArgumentParser(description='Flask App Configuration')
    parser.add_argument('--host', help='Host IP address (default: dynamically determined)')
    parser.add_argument('--port', type=int, default=5000, help='Port number (default: 5000)')
    return parser.parse_args()

# Get host and port from command-line arguments
args = parse_arguments()

# Set up Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET'])
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    if request.method == 'GET':
        # Handle the GET request to display the edit form
        book = Book.query.get_or_404(book_id)
        return render_template('edit.html', book=book)
    elif request.method == 'POST':
        # Handle the POST request to update the book details
        book = Book.query.get_or_404(book_id)
        data = request.form
        new_book_name = data.get('new_book_name')
        new_author = data.get('new_author')
        new_publisher = data.get('new_publisher')

        if new_book_name:
            book.book_name = new_book_name
        if new_author:
            book.author = new_author
        if new_publisher:
            book.publisher = new_publisher

        db.session.commit()
        return redirect(url_for('index'))

@app.route('/update/<int:book_id>', methods=['POST'])
def update_book_info(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.form
    new_book_name = data.get('new_book_name')
    new_author = data.get('new_author')
    new_publisher = data.get('new_publisher')

    if new_book_name:
        book.book_name = new_book_name
    if new_author:
        book.author = new_author
    if new_publisher:
        book.publisher = new_publisher

    db.session.commit()
    return redirect(url_for('index'))

# Routes
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'})

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        book_list.append(book_data)
    return jsonify({'books': book_list})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    book_data = {
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    }
    return jsonify({'book': book_data})

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.book_name = data['book_name']
    book.author = data['author']
    book.publisher = data['publisher']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

# Parse command-line arguments for host and port
def parse_arguments():
    parser = argparse.ArgumentParser(description='Flask App Configuration')
    parser.add_argument('--host', default='127.0.0.1', help='Host IP address')
    parser.add_argument('--port', type=int, default=4000, help='Port number')
    return parser.parse_args()

# Function to start the server in a separate thread
def start_server(host, port):
    app.run(host=host, port=port)

# Function to display the running time
def display_running_time():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        running_time = str(timedelta(seconds=int(elapsed_time)))
        print(f"Server is running for {running_time}", end='\r')
        time.sleep(1)

# Function to handle Ctrl+C gracefully
def signal_handler(sig, frame):
    print("\nServer is shutting down...")
    os._exit(0)  # Forcefully exit the program

# Run the installation
if __name__ == '__main__':
    install_required_packages()
    try:
        with app.app_context():
            db.create_all()

        # Allow the user to input host and port
        host = input(f"Enter host (IP attained automatically[press enter], or input IP here): ") or args.host
        port = input(f"Enter port (default: {args.port}): ") or args.port

        # Time-based Delay
        print("Press Enter to start the program, or wait for 20 seconds for an automatic start...")
        start_time = time.time()
        while True:
            if input() == '' or time.time() - start_time >= 20:
                break

        # If host is not provided, dynamically determine it
        if not host:
            host = socket.gethostbyname(socket.getfqdn())

        # Convert port to an integer
        port = int(port)

        # Register a signal handler for Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        # Start the server in a separate thread
        server_thread = threading.Thread(target=start_server, args=(host, port))
        server_thread.start()

        # Server running confirmation
        print("Thank you! Starting your server")
        print(f"Server is running on http://{host}:{port}/")
        import datetime
        print(f"Server started at {datetime.datetime.now()}")

        # Start the running time display in a separate thread
        running_time_thread = threading.Thread(target=display_running_time)
        running_time_thread.start()

        # Wait for the server thread to finish
        server_thread.join()

    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemy error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        
#    d8b  .d888         d8b 888    888                              .d888 888      
#    Y8P d88P"          Y8P 888    888                             d88P"  888      
#        888                888    888                             888    888      
#   8888 888888 888d888 888 888888 888888 .d8888b          8888b.  888888 888  888 
#   "888 888    888P"   888 888    888    88K                 "88b 888    888 .88P 
#    888 888    888     888 888    888    "Y8888b. 888888 .d888888 888    888888K  
#    888 888    888     888 Y88b.  Y88b.       X88        888  888 888    888 "88b 
#    888 888    888     888  "Y888  "Y888  88888P'        "Y888888 888    888  888 
#    888                                                                           
#   d88P                                                                           
# 888P"                    