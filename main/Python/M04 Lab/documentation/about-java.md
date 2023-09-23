# About JavaScript Script

This document provides a detailed explanation of the JavaScript code used in the Bookstore Database Web Application. The JavaScript code is responsible for handling client-side interactions, making AJAX requests to the server, and dynamically updating the web page.

## `addBook()`

The `addBook()` function is called when the "Add Book" button is clicked on the main page. It collects data from the input fields (book name, author, and publisher), creates a JSON object with the data, and sends it to the server via a POST request to add a new book to the database. After receiving the response, it displays an alert message, clears the form, and refreshes the book list.

## `getBooks()`

The `getBooks()` function retrieves the list of books from the server by making an AJAX GET request to the `/books` endpoint. It populates the table in the HTML with the book data, including book ID, name, author, publisher, and buttons for editing and deleting each book. This function is called initially to load the book list and can be called again to refresh it.

## `editBook(bookId)`

The `editBook(bookId)` function is called when the "Edit" button for a book is clicked. It redirects the user to the edit page for the selected book. The actual implementation of the edit functionality can be done on the edit page.

## `deleteBook(bookId)`

The `deleteBook(bookId)` function is called when the "Delete" button for a book is clicked. It sends an AJAX DELETE request to the server to delete the selected book. After receiving the response, it displays an alert message and refreshes the book list.

## Initial Load

When the web page initially loads, the `getBooks()` function is called to populate the list of books.

This JavaScript code works in conjunction with the server-side logic to provide a seamless user experience for managing book records in the bookstore database.

For more details on how the JavaScript code interacts with the server and the HTML templates, refer to the source code and comments in `app.py` and the HTML templates.
```

You can save this content as `about-javascript.md` and link to it in your `README.md` as explained in the previous response.