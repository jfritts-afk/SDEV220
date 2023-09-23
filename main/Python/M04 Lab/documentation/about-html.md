# `edit.html` - Edit Book Form

The `edit.html` file is an HTML template used in the Bookstore Database Web Application. It provides a form that allows users to edit the details of a specific book. Here's an explanation of the HTML content:

- `<!DOCTYPE html>`: This declaration specifies the document type and version of HTML being used (HTML5).

- `<html>`: The root element of an HTML document.

- `<head>`: The head section contains metadata about the document, including the document's title.

  - `<title>`: Sets the title of the web page to "Edit Book."

- `<body>`: The body section contains the content that will be displayed to the user.

  - `<h1>`: Displays the heading "Edit Book" at the top of the page.

  - `<form>`: Defines an HTML form element used to collect user input. The form's `action` attribute specifies the URL where the form data will be submitted when the user clicks the "Save Changes" button.

    - `action="/edit/{{ book.id }}"`: The `action` attribute is set to `/edit/{{ book.id }}`, where `{{ book.id }}` is a placeholder for the book's unique ID. When the form is submitted, it will send a POST request to the `/edit/<book_id>` endpoint, where `book_id` will be replaced with the actual ID of the book being edited.

    - `method="POST"`: Specifies that the form should use the POST HTTP method to submit data.

  - `<label>`: Labels associated with input fields to describe their purpose.

    - `for="new_book_name"`: The `for` attribute associates the label with the input field with the `id` of "new_book_name."

    - `<input>`: Input fields for editing book details. Each input field has a unique `id` and `name` attribute, which are used to identify the input field in the form. The `value` attribute is set to the corresponding book attribute (e.g., `book.book_name`), which populates the input fields with the book's current information.

    - `required`: The `required` attribute makes the input fields mandatory, ensuring that the user must provide new values for the book's attributes.

  - `<input>`: The "Save Changes" button is an `<input>` element of type "submit." When clicked, it triggers the form submission, sending the updated book details to the server.

  - `<a>`: Provides a link to navigate back to the list of books.

    - `href="/"`: The `href` attribute specifies the URL to which the user will be directed when clicking the link, which is the root URL ("/") leading to the list of books.

The `edit.html` template is used to create a user-friendly interface for editing book details and ensures that the updated information is sent to the server for processing when the form is submitted.

This template is part of the Flask web application's front-end and is used in conjunction with server-side logic to enable users to edit book records in the bookstore database.


# `index.html` - Book Database Main Page

The `index.html` file is an HTML template used as the main page of the Bookstore Database Web Application. It provides a user interface for displaying and managing a list of books in the database. Here's an explanation of the HTML content and associated JavaScript:

- `<!DOCTYPE html>`: This declaration specifies the document type and version of HTML being used (HTML5).

- `<html>`: The root element of an HTML document.

- `<head>`: The head section contains metadata about the document, including the document's title.

  - `<title>`: Sets the title of the web page to "Book Database."

  - `<script>`: Embeds JavaScript code directly into the HTML document.

    - JavaScript Code: This script defines several functions for interacting with the web application and the server via AJAX requests. Here's a summary of the functions:

      - `addBook()`: This function is called when the "Add Book" button is clicked. It collects data from the input fields (book name, author, and publisher), creates a JSON object with the data, and sends it to the server via a POST request to add a new book to the database. After receiving the response, it displays an alert message, clears the form, and refreshes the book list.

      - `getBooks()`: This function retrieves the list of books from the server by making an AJAX GET request to the `/books` endpoint. It populates the table in the HTML with the book data, including book ID, name, author, publisher, and buttons for editing and deleting each book. This function is called initially to load the book list and can be called again to refresh it.

      - `editBook(bookId)`: This function is called when the "Edit" button for a book is clicked. It redirects the user to the edit page for the selected book. The actual implementation of the edit functionality can be done on the edit page.

      - `deleteBook(bookId)`: This function is called when the "Delete" button for a book is clicked. It sends an AJAX DELETE request to the server to delete the selected book. After receiving the response, it displays an alert message and refreshes the book list.

- `<body>`: The body section contains the content that will be displayed to the user.

  - `<h1>`: Displays the heading "Welcome to the Book Database" at the top of the page.

  - `<form>`: Defines an HTML form element used for adding new books to the database.

    - `<label>`: Labels associated with input fields to describe their purpose.

    - `<input>`: Input fields for entering book details (book name, author, publisher). These input fields are used to collect data when adding a new book.

    - `<input type="button">`: The "Add Book" button is an `<input>` element of type "button." When clicked, it triggers the `addBook()` function to add a new book to the database.

  - `<table>`: Displays the list of books in a table format.

    - `<thead>`: Contains table header rows.

      - `<tr>`: Represents a table row containing column headers (ID, Book Name, Author, Publisher, Edit, Delete).

    - `<tbody id="book_list">`: This is the table body where the list of books will be dynamically populated by the JavaScript code. Initially, it's empty, but the `getBooks()` function fills it with book data retrieved from the server.

The `index.html` template provides a user-friendly interface for adding, viewing, editing, and deleting book records in the bookstore database. It uses JavaScript to make asynchronous requests to the server and update the page content dynamically.